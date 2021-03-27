# Suggest Paper Product

## Description
FastAPI has been the framework chosen as it is the Fastest one to be able to startup and do testing


## Requirements
### System Packages (for production deployment)
* Nginx (Web Server)
* Hypercorn (Web server to run the FastAPI application)
* Systemd (To run the application as a system service)
* Certbot (To encrypt the requests and responses to and from the application)

### Python packages (for production deployment and debugging)
* fastapi
* hypercorn
* requests


## Installation
The python packages chosen to carry out the task are as described in the "requirements.txt" file
To be able install those packages it is recomended to create a virtual environment first
This environment will be used together with systemd for production deployment purposes. Nginx will pass on the request to the hypercorn service.

```
python3 -m venv env
```

And activate it with:
```
. ./env/bin/activate
```
if the virtualenv is in the same folder


After the virtual environment has been created we can install the packages with:
```
pip install -r requirements.txt
```

## Starting the server
Hypercorn has been chosen to run the application. The following command should be used to startup the server
```
hypercorn main:app
```
This command should be included in the systemd service definition file, for deployment purposes

## Testing the app
Once the server has been started we can check the application in the web browser using [swagger]('http://localhost:8000/docs')

## Observations
* I tried to make the code as small and neat as possible. I divided separated the code logically (models, database, views(endpoint)). I tried to follow the criteria I learned from Django.
* From README.md I did not get the impression I was supposed to create the Front part.
* No async functionality has been implemented as I didn't have time to optimize the code up to that point
* Tests were done for the Eucledian function and also for the hex_to_rgb and rgb_to_hex functions.
* Those tests were carried out separately as their implementation can be considered independent to the application. I didn't have time to clean them up and include them in the repository
* No Database has been used, I choose the simpler version of using an InMemory Database to save up time
