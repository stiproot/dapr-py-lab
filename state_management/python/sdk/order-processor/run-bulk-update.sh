#!/bin/sh

dapr run --app-id bulk-update \
    --resources-path ../../../resources/ \
    -- python3 bulk_update.py