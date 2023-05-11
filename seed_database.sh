#!/bin/bash

rm db.sqlite3
rm -rf ./baygameapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations baygameapi
python3 manage.py migrate baygameapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata gamers
python3 manage.py loaddata bay_items
python3 manage.py loaddata occasions
python3 manage.py loaddata record_of_trips
python3 manage.py loaddata river_and_streams
python3 manage.py loaddata bay_sites
python3 manage.py loaddata bay_site_items
python3 manage.py loaddata avatars
python3 manage.py loaddata jokes
python3 manage.py loaddata reactions
