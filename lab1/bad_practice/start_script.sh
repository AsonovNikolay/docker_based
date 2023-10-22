#!/bin/sh
docker stop bad_app
docker rm bad_app
docker build -t bad_app --file Bad_dockerfile .
docker run --name bad_app -d -p 1111:1111 bad_app
docker exec bad_app python3 /app/app.py #&>/dev/null &
