#!/bin/sh

gunicorn 'app:create_app()' -w 4 --log-level debug --timeout 5