#!/bin/sh

# uvicorn app:app --host 0.0.0.0 --port 6002

# dapr run --app-id order-processor --resources-path ../../../components/ --app-port 6002 -- python3 app.py

dapr run --app-id order-processor --resources-path ../../../components/ --app-port 6002 -- python3 -m uvicorn app:app --host 0.0.0.0 --port 6002