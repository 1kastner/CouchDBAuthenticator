from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='jupyterhub-couchdb-authenticator',
    version='0.2',
    description='Couchdb Authenticator for JupyterHub',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/1kastner/CouchDBAuthenticator',
    author='Marvin Kastner',
    author_email='marvin.kastner@tuhh.de',
    license='MIT',
    packages=['couchdbauthenticator'],
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)
