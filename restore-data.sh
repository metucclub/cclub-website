#!/bin/bash

if [ ! -z "$1" ]; then
    unzip -o $1

    python manage.py loaddata db.json

    rm db.json
else
    echo "Please define a filename"
fi