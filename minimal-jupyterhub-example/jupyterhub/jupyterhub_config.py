import os
import logging

c.JupyterHub.ssl_key = '/srv/jupyterhub/cert/key.pem'
c.JupyterHub.ssl_cert = '/srv/jupyterhub/cert/cert.pem'

c.JupyterHub.authenticator_class = 'couchdbauthenticator.CouchDBAuthenticator'

c.CouchDBAuthenticator.couchdb_url = "couchdb:6984"
c.CouchDBAuthenticator.ssl_verification = False
c.CouchDBAuthenticator.couchdb_username = os.environ["COUCHDB_USER"]
c.CouchDBAuthenticator.couchdb_password = os.environ["COUCHDB_PASSWORD"]

c.JupyterHub.log_level = logging.DEBUG
