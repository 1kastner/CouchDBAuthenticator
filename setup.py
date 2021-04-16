from setuptools import setup

setup(
    name='jupyterhub-couchdb-authenticator',
    version='0.1b',
    description='Couchdb Authenticator for JupyterHub',
    url='https://github.com/1kastner/jupyterhub-couchdb-authenticator',
    author='Marvin Kastner',
    author_email='marvin.kastner@tuhh.de',
    license='MIT',
    packages=['couchdbauthenticator'],
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)
