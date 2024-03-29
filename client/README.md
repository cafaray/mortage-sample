# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
employee_uuid = 56 # int | UUID of a Employee

try:
    # Delete an Employee with given UUID
    api_response = api_instance.employee_uuid_delete(employee_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->employee_uuid_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://cosafinity-prod.apigee.net/v1/employees*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**employee_uuid_delete**](docs/DefaultApi.md#employee_uuid_delete) | **DELETE** /{employee-uuid} | Delete an Employee with given UUID
*DefaultApi* | [**employee_uuid_get**](docs/DefaultApi.md#employee_uuid_get) | **GET** /{employee-uuid} | Get an Employee with given UUID.
*DefaultApi* | [**employee_uuid_put**](docs/DefaultApi.md#employee_uuid_put) | **PUT** /{employee-uuid} | Update an Employee with given UUID
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Get all Employees
*DefaultApi* | [**root_post**](docs/DefaultApi.md#root_post) | **POST** / | Create a new Employee


## Documentation For Models

 - [Employee](docs/Employee.md)
 - [EmployeesArray](docs/EmployeesArray.md)
 - [EmployeesArrayInner](docs/EmployeesArrayInner.md)
 - [EmployeesArrayInnerMetadata](docs/EmployeesArrayInnerMetadata.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

support@apigee.com

