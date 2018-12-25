#!/bin/sh

python manage.py dumpdata -e auth.permission > db.json

timestamp=$(date +%s)
zip -r "db_$timestamp" media db.json

rm db.json