# Readme

## Building this Image

`docker build -t mycouchdbimage .`

## Starting this Image

`docker run -p 6984:6984 --env-file=../couchdb_credentials.env mycouchdbimage`

## Checking whether it is up

Check the logs, then browse https://localhost:6984 - you need to accept the self-signed certificate.
