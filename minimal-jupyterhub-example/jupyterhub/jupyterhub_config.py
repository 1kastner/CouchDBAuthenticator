import os

c.JupyterHub.authenticator_class = 'couchdbauthenticator.CouchDBAuthenticator'
c.CouchDBAuthenticator.couchdb_url = "couchdb:6984"
c.CouchDBAuthenticator.ssl_verification = False
c.CouchDBAuthenticator.couchdb_username = os.environ["COUCHDB_USER"]
c.CouchDBAuthenticator.couchdb_password = os.environ["COUCHDB_PASSWORD"]
