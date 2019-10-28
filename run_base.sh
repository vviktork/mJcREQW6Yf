#!/bin/bash

docker-compose run web python manage.py migrate

docker-compose run web python manage.py createsuperuser
 
