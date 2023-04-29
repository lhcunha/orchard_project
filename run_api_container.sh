#!/bin/bash
cd /home/orchard_project/api
touch rodei.txt
docker build -t api-image .
docker run --network orchard_project_orchard api-image
