#!/bin/bash
rm -rf /tmp/*.pid
cd app
sleep 15
alembic upgrade head
python -m api.main
