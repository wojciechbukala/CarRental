#!/bin/bash

docker run --rm --name postgres-2 \
--net postgres \
-e POSTGRES_USER=postgresadmin \
-e POSTGRES_PASSWORD=admin123 \
-e POSTGRES_DB=postgresdb \
-e PGDATA="/data" \
-v ${PWD}/postgres-2/pgdata:/data \
-v ${PWD}/postgres-2/config:/config \
-v ${PWD}/postgres-2/archive:/mnt/server/archive \
-p 5002:5432 \
postgres:15.0 -c 'config_file=/config/postgresql.conf'