#!/bin/sh

dapr run --app-id order-processor \
    --resources-path ../../../resources/ \
    -- python3 app.py