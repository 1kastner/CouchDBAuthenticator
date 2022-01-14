"""
Given the CouchDB Docker container, still some settings need to be made manually
after starting the Docker container. This helps to reduce the amount of logged
messages of the CouchDB Docker container.
"""

import warnings
import requests
import dotenv

warnings.filterwarnings('once', message='Unverified HTTPS request')

config = dotenv.dotenv_values("couchdb_credentials.env")
username = config["COUCHDB_USER"]
password = config["COUCHDB_PASSWORD"]
server_url = config["COUCHDB_URL"]  # Assume Docker host to be localhost

# Create CouchDB system database '_users'
# See https://github.com/apache/couchdb-docker#no-system-databases-until-the-installation-is-finalized
# for details.
response = requests.put(
    f"https://{server_url}/_users",
    auth=requests.auth.HTTPBasicAuth(username, password),
    verify=False
)
assert response.status_code in (201, 202), \
    f"Creation of database '_users' failed with status code {response.status_code}, maybe it already exists?"
