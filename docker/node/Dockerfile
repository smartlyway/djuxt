FROM arm32v7/node:6.11.3

MAINTAINER Cristian García <cgardev@gmail.com>

RUN npm install express
RUN npm install vue vue-server-renderer --save
RUN npm install install body-parser
RUN npm install vue-router

WORKDIR /home/docker/code/app/

RUN apk add --update bash && rm -rf /var/cache/apk/*

STOPSIGNAL SIGTERM

