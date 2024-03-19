#!/bin/bash
rm -rf /tmp/*.pid
envsubst < /etc/nginx/nginx.template.conf > /etc/nginx/nginx.conf

cd app
sleep 15
alembic upgrade head
python -m api.main
