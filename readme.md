# todoserver

todo api server based on apiserver-tmpl.

## Instructions
```
source env/bin/activate
```

   * go to /oauth/applications/, Client Type: confidential, Authorization Grant Type: Resource owner password-based
   * curl -v -X POST -d 'client_id=client&client_secret=secret&grant_type=password&username=demo1&password=test123' 'http://localhost:5080/oauth/token/'
   * curl -H 'Authorization: Bearer vafxhqnGkQXBkux6o8HcDPQ8kIZQJ8' 'http://localhost:5080/api/todos'

### run
To run the server
``` ./manage.py runserver 0.0.0.0:8080 ```

## APIs

### User Management

### Todo List Management


