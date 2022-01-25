FROM jupyterhub/jupyterhub:2.1

RUN mkdir /srv/jupyterhub/cert \
    && cd /srv/jupyterhub/cert \
    && openssl req -nodes -x509 -newkey rsa:4096 \
    -keyout key.pem -out cert.pem -days 365 -subj '/CN=my-local-jupyterhub' \
    && chmod 600 key.pem cert.pem \
    && chown nobody key.pem cert.pem

COPY minimal-jupyterhub-example/jupyterhub/jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

COPY . /root/couchdbauthenticator

RUN python3 -m pip --no-cache-dir install notebook \
    && python3 -m pip --no-cache install /root/couchdbauthenticator/ \
    && python3 -c 'import couchdbauthenticator; print(couchdbauthenticator.__version__)' \
    && adduser --disabled-password --gecos '' hey
