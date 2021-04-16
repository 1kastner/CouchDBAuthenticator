"""
Check the activation/deactivation of user accounts.
"""

import os
import sys

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

ssl_verification=True
con = CouchDBConnection(server_url, username, password, ssl_verification=False)

if len(sys.argv) <=2 or sys.argv[1] not in ('reactivate', 'deactivate'):
    print("provide either the command 'reactivate' or 'deactivate' followed by at least one username")
    sys.exit()

invocation = {
    "reactivate" : con.reactivate_user,
    "deactivate" : con.deactivate_user
}[sys.argv[1]]

for username in sys.argv[2:]:
    invocation(username)
