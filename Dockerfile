FROM openmason/fleet-nginx:latest

RUN echo 'root:test123' | chpasswd

RUN mkdir /deploy
WORKDIR /deploy
ADD . /deploy/
RUN \
  apt-get update; \
  apt-get install -yq \
      libpq-dev libffi-dev
RUN pip install -r requirements.txt

#CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]
