FROM openmason/fleet-nginx:latest

RUN echo 'root:test123' | chpasswd

RUN     mkdir /deploy
WORKDIR       /deploy
ADD     .     /deploy/

ADD conf/nginx   /etc/nginx/sites-enabled
ADD conf/circus/conf.d/todoserver.conf  /etc/circus/conf.d/todoserver.conf

RUN  apt-get update; \
     apt-get install -yq \
       libpq-dev postgresql-client-common postgresql-client-9.3 \
       libffi-dev binutils libproj-dev gdal-bin libgeoip1 python-gdal;

RUN  pip install -r requirements.txt

#CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
