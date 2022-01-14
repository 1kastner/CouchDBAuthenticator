FROM jupyterhub/jupyterhub:1.3

RUN pip --no-cache-dir install notebook

RUN mkdir /srv/jupyterhub/cert \
    && cd /srv/jupyterhub/cert \
    && openssl req -nodes -x509 -newkey rsa:4096 \
    -keyout key.pem -out cert.pem -days 365 -subj '/CN=my-local-jupyterhub' \
    && chmod 600 key.pem cert.pem \
    && chown nobody key.pem cert.pem

COPY minimal-jupyterhub-example/jupyterhub/jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

COPY . /root/couchdbauthenticator

RUN pip install -e /root/couchdbauthenticator \
    && adduser --disabled-password --gecos '' hey
