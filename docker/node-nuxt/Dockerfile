FROM node:7.10.1-alpine

MAINTAINER Cristian García <cgardev@gmail.com>

RUN npm install -g express
RUN npm install -g vue vue-server-renderer vue-router vue-cli
RUN npm install -g body-parser

WORKDIR /home/docker/code/app/

RUN apk add --update bash && rm -rf /var/cache/apk/*

CMD exec /bin/bash -c "trap : TERM INT; sleep 500000 & wait"
