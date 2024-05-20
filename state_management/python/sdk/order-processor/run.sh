#!/bin/sh

# dapr run --app-id order-processor \
dapr run --app-id bulk-update \
    --resources-path ../../../resources/ \
    -- python3 bulk_update.py
    # -- python3 app.py

    # --app-port 5000 \
    # --dapr-http-port 3601 \

# dapr run --app-id demo \
#     --app-port 5000 \
#     --dapr-http-port 3500 \
#     --resources-path ../../../resources/