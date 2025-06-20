#!/bin/bash

echo "Decoding Base64 SQL..."
base64 -d /docker-entrypoint-initdb.d/init.sql.b64 > /docker-entrypoint-initdb.d/init.sql

echo "Starting MySQL..."
exec docker-entrypoint.sh mysqld
