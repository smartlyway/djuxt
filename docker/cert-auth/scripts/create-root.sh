#!/bin/bash

cd /root/ca/ && \

openssl genrsa -aes256 -out private/ca.key.pem 4096 && \

chmod 400 private/ca.key.pem && \

openssl req -config openssl.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem && \

chmod 444 certs/ca.cert.pem && \

openssl x509 -noout -text -in certs/ca.cert.pem && \

cp /root/ca/certs/ca.cert.pem /home/export/ca.cert.pem