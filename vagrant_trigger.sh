#!/bin/bash

pwd
cd /vagrant
pwd

poetry install
nohup poetry run flask run > logs.txt 2>&1 &