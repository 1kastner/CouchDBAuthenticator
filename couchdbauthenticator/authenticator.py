from tornado import gen
from jupyterhub.auth import Authenticator
from traitlets import Unicode

import requests

class CouchDBAuthenticator(Authenticator):
    """
    All code needs to be recycled
    """

    couchdb_url = Unicode(
        help='URL to visit the CouchDB server',
        config=True
    )

    couchdb_username = Unicode(
        help='username to log into the CouchDB server',
        config=True
    )

    couchdb_password = Unicode(
        help='password to log into the CouchDB server',
        config=True
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        provided_password = data['password']

        # Query CouchDB
        search_url = f"http://{self.couchdb_username}:{self.couchdb_password}@{self.couchdb_url}/users/_find"
        query = {
            "selector" : {
                "username" : username,
                "active" : True
            },
            "fields" : ["username", "password"],
            "limit" : 1
        }
        response = requests.post(search_url, json=query)
        parsed_response = response.json()

        if len(parsed_response["docs"]) == 0:
            self.log.warn(f"provided user name '{username}' not existent")
            return
        retrieved_user = parsed_response["docs"][0]
        actual_password = retrieved_user["password"]
        if actual_password != provided_password:
            self.log.warn(f"provided password of '{username}' did not match")
            return
        
        self.log.debug("User '{provided_username}' logged in")
        return username
