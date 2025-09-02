#!/usr/bin/env bash

pyenv activate cblab

./src/manage.py runserver 8002 || ./src/manage.py runserver 8003