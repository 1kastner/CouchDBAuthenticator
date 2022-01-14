"""
Check the activation/deactivation of user accounts.
"""

import sys
import warnings
import dotenv

from couchdbauthenticator.user_manager import CouchDBConnection

warnings.filterwarnings('once', message='Unverified HTTPS request')

config = dotenv.dotenv_values("couchdb_credentials.env")
username = config["COUCHDB_USER"]
password = config["COUCHDB_PASSWORD"]
server_url = config["COUCHDB_URL"]  # Assume Docker host to be localhost

con = CouchDBConnection(server_url, username, password, ssl_verification=False)

if len(sys.argv) <= 2 or sys.argv[1] not in ('reactivate', 'deactivate'):
    print("provide either the command 'reactivate' or 'deactivate' followed by at least one username")
    sys.exit()

invocation = {
    "reactivate": con.reactivate_user,
    "deactivate": con.deactivate_user
}[sys.argv[1]]

usernames_to_deactivate = sys.argv[2:]
print("Deactivate users:")
for username in usernames_to_deactivate:
    print("- " + username)
    invocation(username)
