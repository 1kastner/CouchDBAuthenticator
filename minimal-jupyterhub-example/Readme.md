# Minimal JupyterHub Example

This example is only for illustration how the components play together.
It is inertly insecure and it is not designed to scale.
Please use proper SSL certificates and configuration!

The CouchDB spawns at https://localhost:6984 with a self-signed certificate.
Visit https://localhost:6984/_utils for a Web UI.
The credentials are stored in the file couchdb_credentials.

The JupyterHub spawns at https://localhost:8000 with a self-signed certificate.
First, you can't log in.
But there is `seed_users_database.py` which will do the following:
- Create a database called 'users'
- Make it only accessible to the CouchDB user used for authentication (here, the CouchDB admin account)
- Create the user 'hey' with the password 'pss'
You can check the result in the CouchDB Web UI (see previous paragraph).

Now you can use the user 'hey' to log into the JupyterHub.
If you are annoyed by all the logging the CouchDB does, you might want to run
`configure_couchdb.py` to silence those warnings.

If you want to disable the account without permanently deleting username and password, you can use `control_users_database.py`.
With that command line tool you can deactivate and reactivate accounts.
Be aware that any change only affects new login attempts.
If a user still has an open session, it will not be affected.
