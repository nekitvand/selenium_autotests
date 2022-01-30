#!/bin/bash

docker network create selenoid || True
docker-compose up -d
sleep 5
docker exec -i ui-autotests python load.py
