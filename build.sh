#!/bin/sh
docker build -t sso_token_service:v0.0.1 .
docker run -d --rm -p 10086:10086 --name sso_token_service sso_token_service:v0.0.1