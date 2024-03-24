#!/bin/bash
rm -rf /tmp/*.pid
cd app
sleep 20
alembic upgrade head
python -m api.main
