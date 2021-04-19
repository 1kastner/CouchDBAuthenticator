"""
Seed the CouchDB 'users' database for the authenticator.
"""

import os
import sys
import warnings
warnings.filterwarnings('once', message='Unverified HTTPS request')

import dotenv

sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.pardir
))

from couchdbauthenticator.user_manager import CouchDBConnection

config = dotenv.dotenv_values("couchdb_credentials.env")
username = config["COUCHDB_USER"]
password = config["COUCHDB_PASSWORD"]

# Assume Docker host to be localhost
server_url = "localhost:6984"

con = CouchDBConnection(server_url, username, password, ssl_verification=False)
con.reset_users_database()
con.restrict_access_to_couchdb_user()
con.add_new_user("hey", "pss")
