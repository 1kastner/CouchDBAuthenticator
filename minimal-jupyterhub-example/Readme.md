# Minimal JupyterHub Example

This example is only for illustration how the components play together.
It is inertly insecure and it is not designed to scale.
Please use proper SSL certificates and configuration!
This minimal example is used, among others, for the development and the integration testing of the code.

## Preparatory Steps
The scripts below have additional dependencies.
Please install them by running `pip install -e ..[example]` in this directory.
Moreover, you might want to adjust the default credentials of the CouchDB.
For this, open the file `couchdb_credentials.env` and replace the credentials.

## Start Example JupyterHub
Run `docker-compose up --build --force-recreate` on the project root level (i.e. the parent directory of this file).
This automatically starts the required Docker containers.
- The CouchDB spawns at https://localhost:6984 with a self-signed certificate.
  Visit https://localhost:6984/_utils for a Web UI.
  Authenticate yourself with the credentials from `couchdb_credentials.env`.
- The JupyterHub spawns at https://localhost:8000 with a self-signed certificate.
  First, you can't log in as no user has yet been properly set up.

## Create Default User
For the next step, there is `seed_users_database.py` which will do the following:
- Create a database called 'users'
- Make it only accessible to the CouchDB user used for authentication (here, the CouchDB admin account)
- Create the user 'hey' with the password 'pss'
You can check the result in the CouchDB Web UI.
Feel free to adjust the credentials in `seed_users_database.py`.

## Improve the Experience
Now you can use the user 'hey' to log into the JupyterHub.
If you are annoyed by all the logging the CouchDB does, you might want to run
`configure_couchdb.py` to silence those warnings.

If you want to disable the account without permanently deleting username and password, you can use `control_users_database.py`.
With that command line tool you can deactivate and reactivate accounts.
Be aware that any change only affects new login attempts.
If a user still has an open session, it will not be affected.
First, ensure that the user 'hey' is logged out.
Then you can run
`python ./control_users_database.py deactivate hey`
to disable the login of that user.
If you want to reactivate a user account, simply run
`python ./control_users_database.py reactivate hey`.
