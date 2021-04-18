"""
A client API to manage the user accounts of the CouchDBAuthenticator.
"""

import requests

class CouchDBConnection:
    """
    See the following for more information:
    - https://docs.couchdb.org/en/stable/api/database/common.html
    - https://docs.couchdb.org/en/stable/intro/security.html
    """

    def __init__(self, server_url, username, password, ssl_verification=True):
        """
        The username and password are used to log into the CouchDB.
        As the database 'users' is deleted and recreated, that user must be
        an administrator of the CouchDB.
        """
        self.server_url = f"https://{server_url}/"
        self.username = username
        self.auth = requests.auth.HTTPBasicAuth(username, password)
        self.ssl_verification = ssl_verification

    def reset_users_database(self):
        """
        (Re-)Creates the database 'users'
        """
        response_1 = requests.delete(self.server_url + "users", auth=self.auth, verify=self.ssl_verification)
        assert response_1.status_code in (200, 202, 404), "Deletion of database 'users' failed"
        response_2 = requests.put(self.server_url + "users", auth=self.auth, verify=self.ssl_verification)
        assert response_2.status_code in (201, 202), "Creation of database 'users' failed"

    def restrict_access_to_couchdb_user(self):
        """
        Cited from the documentation at https://docs.couchdb.org/en/latest/api/database/security.html

        > Having no admins, only server admins (with the reserved _admin role) are able to update design
        > document and make other admin level changes.
        >
        > Having no members, any user can write regular documents (any non-design document) and read documents
        > from the database.
        """
        security_endpoint = self.server_url + "/users/_security"
        security_document = {
            "admins":{
                "names": []
            },
            "members":{
                "names": [self.username]
            },
        }
        response_1 = requests.put(security_endpoint, json=security_document, auth=self.auth, 
            verify=self.ssl_verification)
        assert response_1.status_code == 200, "Security documet could not be inserted"
        response_2 = requests.get(self.server_url + "users", verify=self.ssl_verification)
        assert response_2.status_code == 401, "Database still accessible from unauthenticated users"

    def add_new_user(self, username, password):
        """
        Adds new user document to the users database.
        """
        user_doc = {
            "username": username,
            "password": password,
            "active": True
        }
        response = requests.post(self.server_url + "users", auth=self.auth, verify=self.ssl_verification,
            json=user_doc)
        assert response.status_code in (201, 202), "User could not be created"

    def _find_user(self, username):
        """
        Find user in database.
        """
        search_url = self.server_url + "/users/_find"
        query = {
            "selector" : {
                "username" : username
            },
            "limit" : 1
        }
        response = requests.post(search_url, json=query, auth=self.auth, verify=self.ssl_verification)
        parsed_response = response.json()
        user_doc = parsed_response["docs"][0]
        return user_doc

    def deactivate_user(self, username):
        user_doc = self._find_user(username)
        user_doc["active"] = False
        response = requests.put(self.server_url + "users/" + user_doc["_id"], 
            auth=self.auth, verify=self.ssl_verification,
            json=user_doc)
        assert response.status_code in (201, 202), "User document could not be updated"
        
    def reactivate_user(self, username):
        user_doc = self._find_user(username)
        user_doc["active"] = True
        response = requests.put(self.server_url + "users/" + user_doc["_id"], 
            auth=self.auth, verify=self.ssl_verification,
            json=user_doc)
        assert response.status_code in (201, 202), "User document could not be updated"
