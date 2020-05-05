#!/bin/sh
nginx
gunicorn --bind=127.0.0.1:8930 --workers=2 educator.wsgi:application