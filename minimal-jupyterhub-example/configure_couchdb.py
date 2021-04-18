"""
Do some settings to reduce the logging.
"""

import requests
import dotenv

config = dotenv.dotenv_values("couchdb_credentials.env")
username = config["COUCHDB_USER"]
password = config["COUCHDB_PASSWORD"]

# Assume Docker host to be localhost
server_url = "https://localhost:6984/"

response_1 = requests.put(server_url + "_users", auth=requests.auth.HTTPBasicAuth(username, password), verify=False)
assert response_1.status_code in (201, 202), "Creation of database '_users' failed"
