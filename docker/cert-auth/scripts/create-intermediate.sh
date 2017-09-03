#!/bin/bash

cd /root/ca && \

openssl genrsa -aes256 \
      -out intermediate/private/intermediate.key.pem 4096 && \

chmod 400 intermediate/private/intermediate.key.pem && \

openssl req -config intermediate/openssl.cnf -new -sha256 \
      -key intermediate/private/intermediate.key.pem \
      -out intermediate/csr/intermediate.csr.pem && \

openssl ca -config openssl.cnf -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in intermediate/csr/intermediate.csr.pem \
      -out intermediate/certs/intermediate.cert.pem  && \

chmod 444 intermediate/certs/intermediate.cert.pem && \

cat intermediate/certs/intermediate.cert.pem \
      certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem && \

chmod 444 intermediate/certs/ca-chain.cert.pem && \

cp /root/ca/intermediate/certs/intermediate.cert.pem /home/export/intermediate.cert.pem