# CouchDB Authenticator for JupyterHub

This is a simple authenticator for a [JupyterHub](http://github.com/jupyter/jupyterhub/)
that fetches user authentication information from a CouchDB over HTTPS.
This authenticator is designed for events where the organizer distributes
usernames and passwords to the participants and they are not meant to be able to change them.
This authenticator harmonizes well with a system user agnostic spawner such as 
[dockerspawner](https://github.com/jupyterhub/dockerspawner) which allow the whole JupyterHub
to be torn down after the besaid event without the need of deleting operating system users.

## CouchDB Document Format

The authenticator expects that on the CouchDB server a database called `users` exist.
Each user is expected to be a document with the fields `username`, `password_hash`, and `active`.
The password_hash must be a hex representation of a [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2)
derived hash of the password, using the username as salt.
The PBKDF2 iteration count is configurable, and defaults to 1000.

## Security Notes

If you need your JupyterHub installation to be highly secure, do *not* use this authenticator!
It trades off some security for a lot of convenience,
which might or might not be the right tradeoff for your JupyterHub installation.

## Logging people out

If you make any changes to JupyterHub's authentication setup
that changes which group of users is allowed to login 
(such as changing the csv url, removing access for individual users, or even just turning on a new authenticator),
you *have* to change the jupyterhub cookie secret, 
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
c.JupyterHub.authenticator_class = couchdbauthenticator.CouchDBAuthenticator'
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

## Development

When you want to try out the current installer, on the project root level you can run
`docker-compose up --build --force-recreate`.
This automatically sets up a minimal jupyterhub example with this authenticator.
