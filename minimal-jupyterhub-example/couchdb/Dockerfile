FROM couchdb:latest

RUN mkdir /etc/couchdb/cert && cd /etc/couchdb/cert

COPY local.ini.extension /etc/couchdb/cert/local.ini.extension

RUN cd /etc/couchdb/cert \
    && openssl req -nodes -x509 -newkey rsa:4096 \
    -keyout key.pem -out cert.pem -days 365 -subj '/CN=mylocalcouchdb' \
    && chmod 600 key.pem cert.pem \
    && chown couchdb key.pem cert.pem

RUN cat /etc/couchdb/cert/local.ini.extension >> /opt/couchdb/etc/local.ini
