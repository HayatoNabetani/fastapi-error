#!/bin/bash
cd /workspace/app/db
alembic upgrade head
cd /workspace
uvicorn app.main:app --reload --port=8000 --host=0.0.0.0
