import os

c.JupyterHub.authenticator_class = 'couchdbauthenticator.CouchDBAuthenticator'
c.CouchDBAuthenticator.couchdb_url = "couchdb:5984"
c.CouchDBAuthenticator.couchdb_username = os.environ["COUCHDB_USER"]
c.CouchDBAuthenticator.couchdb_password = os.environ["COUCHDB_PASSWORD"]
