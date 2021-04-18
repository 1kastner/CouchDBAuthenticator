# CouchDB Authenticator for JupyterHub

This is a simple authenticator for a [JupyterHub](http://github.com/jupyter/jupyterhub/)
that fetches user authentication information from a CouchDB over HTTPS.
This authenticator is designed for events where the organizer distributes
usernames and passwords to the participants and they are not meant to be able to change them.
The event is supposed to only last for a short time and the sole purpose of authentication
is that the JupyterHub can tell the different users apart.
This authenticator harmonizes well with a system user agnostic spawner such as 
[dockerspawner](https://github.com/jupyterhub/dockerspawner) which allow the whole JupyterHub
to be torn down after the besaid event without the need of deleting operating system users.
The code of this project has been inspired by the 
[Remote CSV Authenticator](https://github.com/yuvipanda/jupyterhub-remotecsv-authenticator).

## CouchDB Document Format

The authenticator expects that on the CouchDB server a database called `users` exist.
Each user is expected to be a document with the fields `username`, `password`, and `active`.
The values of `username` and `password` are plaintext, the field `active` is boolean.
This approach does not hash the password.
Each password should be randomly generated by the event organizer and it should be sufficiently complex.

## Security Notes

If you need your JupyterHub installation to be highly secure, do *not* use this authenticator!
It trades off some security for a lot of convenience,
which might or might not be the right tradeoff for your JupyterHub installation.

## Logging people out

If you make any changes to JupyterHub's authentication setup
that changes which group of users is allowed to login 
(such as changing the CouchDB, removing access for individual users, or even just turning on a new authenticator),
you *have* to change the JupyterHub cookie secret, 
or users who were previously logged in and did not log out would continue to be logged in!

You can do this by deleting the `jupyterhub_cookie_secret` file. 
Note that this will log out *all* users who are currently logged in.

## Installation

```
pip install jupyterhub-couchdb-authenticator
```

You can then use this as your authenticator by adding the following line to
your `jupyterhub_config.py`:

```
c.JupyterHub.authenticator_class = 'couchdbauthenticator.CouchDBAuthenticator'
```

## Configuration

Don't forget the preceeding `c.` for setting configuration parameters! 
JupyterHub uses
[traitlets](https://traitlets.readthedocs.io) for 
configuration, and the `c` represents the
[config object](https://traitlets.readthedocs.io/en/stable/config.html).

- `CouchDBAuthenticator.couchdb_url`: 
  The url where to reach the CouchDB.
- `CouchDBAuthenticator.couchdb_username`: 
  The username for log into the CouchDB so that
  one has read access to the `users` database.
- `CouchDBAuthenticator.couchdb_password`: 
  The password belonging to the username above.
  It is adviced to use environment variables and *not* to
  hardcode the credentials into the configuration.

## Adding and Deactivating Users

You can create, modify and delete users in the CouchDB Web UI manually.
Furthermore, you can use any REST API tool, see 
[the CouchDB manual](https://docs.couchdb.org/en/stable/api/basics.html)
for more information.
In `couchdbauthenticator.user_manager`, the class `CouchDBConnection` resides.
This is for pure convenience.
See `minimal-jupyterhub-example/seed_users_database.py` and `minimal-jupyterhub-example/control_users_database.py`
for some sample applications.

## Minimal Example and Development

For running the mininmal example, you need to clone the GitHub repository.
Check
[this explanation](https://github.com/1kastner/CouchDBAuthenticator/tree/main/minimal-jupyterhub-example)
for more insights.
