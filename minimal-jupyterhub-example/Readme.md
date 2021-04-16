# Minimal JupyterHub Example

This example is only for illustration how the components play together.
It is inertly insecure and it is not designed to scale.
Please use proper SSL certificates and configuration!

The CouchDB spawns at https://localhost:6984 with a self-signed certificate.
Visit https://localhost:6984/_utils for a Web UI.
The credentials are stored in the file couchdb_credentials.

The JupyterHub spawns at http://localhost:8000 without any encryption.
