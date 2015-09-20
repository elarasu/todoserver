FROM openmason/fleet-nginx:latest

RUN echo 'root:test123' | chpasswd

# install postgres related pkgs
RUN \
    apt-get update; \
    apt-get install -yq \
       libpq-dev postgresql-client-common postgresql-client-9.3 \
       libffi-dev binutils libproj-dev gdal-bin libgeoip1 python-gdal \
       --no-install-recommends;

# copy required configurations
ADD conf/nginx/todoserver   /etc/nginx/sites-enabled/todoserver
ADD conf/circus/conf.d/todoserver.conf  /etc/circus/conf.d/todoserver.conf

# deploy django code
RUN     mkdir /deploy
WORKDIR       /deploy
ADD     .     /deploy/

# Install django
RUN pip install --upgrade pip
RUN pip install --upgrade -r  requirements.txt


#CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
