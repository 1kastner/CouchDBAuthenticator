"""
The authenticator code that is used on the JupyterHub for authenticating people by the entries in a database.
"""

from tornado import gen
from jupyterhub.auth import Authenticator
from traitlets import Unicode, Bool
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

    ssl_verification = Bool(
        help='switch off ssl verification to support self-signed certificates in development environments',
        config=True
    )


    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        provided_password = data['password']

        # Query CouchDB
        search_url = f"https://{self.couchdb_url}/users/_find"
        query = {
            "selector" : {
                "username" : username,
                "active" : True
            },
            "fields" : ["username", "password"],
            "limit" : 1
        }
        response = requests.post(search_url, json=query, 
            auth=requests.auth.HTTPBasicAuth(self.couchdb_username, self.couchdb_password),
            verify=self.ssl_verification)
        parsed_response = response.json()

        if not hasattr(parsed_response, "keys") or "docs" not in parsed_response.keys():
            raise Exception(f"Malformed response of CouchDB search query: '{response}'")

        if len(parsed_response["docs"]) == 0:
            self.log.info(f"provided user name '{username}' not existent")
            return
        retrieved_user = parsed_response["docs"][0]
        actual_password = retrieved_user["password"]
        if actual_password != provided_password:
            self.log.info(f"provided password of '{username}' did not match")
            return
        
        self.log.debug("User '{provided_username}' logged in")
        return username
