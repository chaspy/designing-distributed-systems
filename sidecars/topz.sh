#!/bin/bash
APP_ID=${1}
docker run --pid=container:${APP_ID} \
  -p 8080:8080 \
   brendanburns/topz:db0fa58 \
   /server -addr=0.0.0.0:8080

