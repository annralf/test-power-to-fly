#!/bin/sh

gunicorn -b 0.0.0.0:80 'app:create_app()' --log-level debug --timeout 5