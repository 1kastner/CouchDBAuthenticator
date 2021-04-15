FROM jupyterhub/jupyterhub:1.3

RUN pip install notebook jupyterhub-systemdspawner

COPY minimal-jupyterhub-example/jupyterhub/jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

COPY . /root/

RUN pip install -e /root/

RUN adduser --disabled-password --gecos '' hey
