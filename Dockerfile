FROM openmason/fleet-nginx:latest

RUN echo 'root:test123' | chpasswd

RUN     mkdir /deploy
WORKDIR       /deploy
ADD     .     /deploy/
ADD     conf  /etc/

RUN  apt-get update; \
     apt-get install -yq libpq-dev libffi-dev; \
     pip install --upgrade pip; \
     pip install virtualenv
RUN  virtualenv env
RUN  . env/bin/activate
RUN  pip install -r requirements.txt

#CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
