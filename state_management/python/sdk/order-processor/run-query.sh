#!/bin/sh

dapr run --app-id query \
    --resources-path ../../../resources/ \
    -- python3 query.py