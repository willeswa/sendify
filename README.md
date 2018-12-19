[![Coverage Status](https://coveralls.io/repos/github/willeswa/sendify/badge.svg?branch=develop)](https://coveralls.io/github/willeswa/sendify?branch=develop)  <a href="https://codeclimate.com/github/willeswa/sendify/maintainability"><img src="https://api.codeclimate.com/v1/badges/b4e642ff7cf263b084d6/maintainability" /></a>  [![Build Status](https://travis-ci.com/willeswa/sendify.svg?branch=develop)](https://travis-ci.com/willeswa/sendify)  [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b7c3c5956d48430590caf3875d257d26)](https://www.codacy.com/app/willeswa/sendify?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=willeswa/sendify&amp;utm_campaign=Badge_Grade)
## Send-It-API
Sendify API is an appliaction that allows users to create parcels and track the parcels from pick up to destination.

This project shows one of the possible ways to implement RESTful API server.

### Running 

1. Clone repository.

https://github.com/willeswa/sendify.git

#### Create and activate a virtual environment

    `virtualenv env --python=python3.6`

    `source env/bin/activate`

#### Install required Dependencies

    pip install -r requirements.txt

### Running the application

```
$ export FLASK_APP="run.py"
$ export FLASK_ENV="development"
$ flask run
```

#### Open postman and use the below endpoints.


### Endpoints currently available

| Method    | Endpoint                              | Description                           | User-type         |
| --------- | ------------------------------------- |-------------------------------------- | ----------------- |
|1.POST     | /api/v2/parcels                       | Creates a new parcel order.           | customers         |
|2.GET      | /api/v2/parcels                       | Get all parcel orders                 | admin             |
|3.GET      | /api/v2/parcels/int                   | Get a specific parcel order           | customers/admin   |
|4.PUT      | /api/v2/parcels/int/destination       | Change a parcel's destination         | customers         |
|5.PUT      | /api/v2/parcels/int/presentloaction   | changes parcel current location       | admin             |
|5.PUT      | /api/v2/parcels/int/status            | changes the status of a parcel        | admin             |
|6.GET      | /api/v2/users/int/parcels             | gets parcels by specific users        | customer          |
|7.POST     | /api/v2/auth/signup                   | Registers a user to the app           | customers         |
|9.POST     | /api/v2/auth/login                    | Logs in a user to the app             | Admin/customer    |  

### How to test the hosted version:
Heroku app hosted on: 
https://sendify-app.herokuapp.com/api/v1/
place the different endpoints at the end of the above url to test


### Created with :two_hearts: by:
<a href='https://github.com/willeswa'>Willies Wanjala</a>

<a href="http://flask.pocoo.org/"><img
   src="http://flask.pocoo.org/static/badges/powered-by-flask-s.png"
   border="0"
   alt="powered by Flask"
   title="powered by Flask"></a>
