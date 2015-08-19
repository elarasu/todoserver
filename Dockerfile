FROM openmason/fleet-nginx:latest

RUN echo 'root:test123' | chpasswd

RUN     mkdir /deploy
WORKDIR       /deploy
ADD     .     /deploy/

ADD conf/nginx     /etc/nginx/sites-enabled
ADD conf/circus    /etc/circus

RUN  apt-get update; \
     apt-get install -yq libpq-dev libffi-dev golang; \
     pip install --upgrade pip
RUN  pip install -r requirements.txt

#CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
