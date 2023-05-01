#!/bin/bash
cd /home/orchard_project/api
touch run_log.txt
docker build -t api-image .
docker run --network orchard_project_orchard api-image
