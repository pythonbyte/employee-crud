# Onyo Challenge

# Description

This project is a challenge for a job opening at Onyo. It's a CRUD for employees

Deployed app at Heroku: https://employeecrud.herokuapp.com/
# Installing

First step of installation is having Pipenv installed in your machine, if you doesn't have just use the command below:

``` $ pip install pipenv ```

Now after cloned the repository all you need to do is:

```
$ cd employeecrud/
$ pipenv install
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Testing

To test the application use:

```$ python manage.py test```


# API documentation

This API works with 2 simple endpoints:

## Employees Endpoint
This endpoint works at the **/employees**, and lists the employees created and create new employees.

GET data:
Status: 200 OK
```
[
    {
        "id": 1,
        "email": "teste@hot.com",
        "job_role": "Developer",
        "name": "Teste do Teste",
        "phone": "31999999999",
        "cep": "30330330",
        "city": "Belo Horizonte",
        "local_address": "Rua Campo Belo",
        "neighborhood": "São Pedro",
        "number": 15,
        "state": "MG"
    }
]
```

Post data:
In the post data in order to use the zipcode api is required to send the fields cep and number.
```
{
    "name": "Teste do Teste",
    "email": "teste@hot.com",
    "job_role": "Developer",
    "phone": "31999999999",
    "cep": "30330330",
    "number": "15"
}
```
Response data:
Status: 201 Created
```
[
    {
        "id": 1,
        "email": "teste@hot.com",
        "job_role": "Developer",
        "name": "Teste do Teste",
        "phone": "31999999999",
        "cep": "30330330",
        "city": "Belo Horizonte",
        "local_address": "Rua Campo Belo",
        "neighborhood": "São Pedro",
        "number": 15,
        "state": "MG"
    }
]
```
## Employee Detail Endpoint
This endpoint works at the **/employees/id** . This endpoint show the detail of a specific employee and you can Modify or Delete the object using the methods PUT and DELETE.

Get data and Put Data response:
url: '/employees/1'
Status: 200 OK
```
{
    "id": 1,
    "email": "teste@hot.com",
    "job_role": "Developer",
    "name": "Teste do Teste",
    "phone": "31999999999",
    "cep": "30330330",
    "city": "Belo Horizonte",
    "local_address": "Rua Campo Belo",
    "neighborhood": "São Pedro",
    "number": 15,
    "state": "MG"
}
```
Delete response:
Status: 204 No Content
```
{
  'message': 'User Teste do Teste was deleted.'
}

