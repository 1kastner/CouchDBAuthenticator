"""
Seed the CouchDB 'users' database for the authenticator.
"""

import warnings
import dotenv

from couchdbauthenticator.user_manager import CouchDBConnection

warnings.filterwarnings('once', message='Unverified HTTPS request')

config = dotenv.dotenv_values("couchdb_credentials.env")
username = config["COUCHDB_USER"]
password = config["COUCHDB_PASSWORD"]
server_url = config["COUCHDB_URL"]  # Assume Docker host to be localhost

con = CouchDBConnection(server_url, username, password, ssl_verification=False)
con.reset_users_database()
con.restrict_access_to_couchdb_user()
con.add_new_user("hey", "pss")
