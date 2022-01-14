RMDIR /s build dist jupyterhub_couchdb_authenticator.egg-info

CALL python setup.py sdist bdist_wheel

CALL twine check .\dist\*

ECHO With 'twine upload dist/*', you upload the new version now.
