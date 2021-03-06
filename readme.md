# todoserver

todo api server based on apiserver-tmpl.

## init
```
psql -h postgres -U docker postgres
DROP DATABASE todos;
CREATE DATABASE todos;
psql -h postgres -U docker todos
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
python manage.py collectstatic
python manage.py loaddata fixtures/sites.json
python manage.py loaddata fixtures/oauth2_provider.json

```


## Setup
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py syncdb
```

## Instructions
```
source env/bin/activate
```

   * go to /oauth/applications/, Client Type: confidential, Authorization Grant Type: Resource owner password-based
   * python manage.py loaddata oauth2_provider.json

### oauth token

   * curl -X POST -d 'client_id=client&client_secret=secret&grant_type=password&username=demo1&password=test123' 'http://localhost:4080/oauth/token/'
   * export AUTH_HDR='Authorization: Bearer <access-token-here>'

### save oauth fixture

   * python manage.py dumpdata oauth2_provider.application > fixtures/oauth2_provider.application

### run
To run the server
```
export MQTT_HOST='192.168.1.13'
./manage.py runserver 0.0.0.0:4080
```

## APIs

### User Management

### Todo List Management

   * curl -X GET     -H "$AUTH_HDR" 'http://localhost:4080/api/todos'
   * curl -X POST    -H "$AUTH_HDR" 'http://localhost:4080/api/todos' --data 'task=where'
   * curl -X PUT     -H "$AUTH_HDR" 'http://localhost:4080/api/todos/2' --data 'task=changed+here'
   * curl -X DELETE  -H "$AUTH_HDR" 'http://localhost:4080/api/todos/2'


## Todo

    * circusweb to be fixed
    * upgrade to postgrest 9.5
    * upgrade to python3
    * set password and db stuff from environment variables
