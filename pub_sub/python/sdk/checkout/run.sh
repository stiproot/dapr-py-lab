#!/bin/sh

dapr run --app-id checkout --resources-path ../../../components/ -- python3 app.py