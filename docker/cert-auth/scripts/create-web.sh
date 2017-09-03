#!/bin/bash

readonly MAIN_URL="djuxt.local"

cd /root/ca && \

openssl genrsa -aes256 \
      -out intermediate/private/${MAIN_URL:?}.key.pem 2048  && \

chmod 400 intermediate/private/${MAIN_URL:?}.key.pem   && \

openssl req -config intermediate/web-openssl.cnf \
      -key intermediate/private/${MAIN_URL:?}.key.pem \
      -new -sha256 -out intermediate/csr/${MAIN_URL:?}.csr.pem && \

openssl ca -config intermediate/web-openssl.cnf \
      -extensions server_cert -days 375 -notext -md sha256 \
      -in intermediate/csr/${MAIN_URL:?}.csr.pem \
      -out intermediate/certs/${MAIN_URL:?}.cert.pem && \

chmod 444 intermediate/certs/${MAIN_URL:?}.cert.pem && \

cp /root/ca/intermediate/certs/${MAIN_URL:?}.cert.pem /home/export/${MAIN_URL:?}.cert.pem && \
cp /root/ca/intermediate/certs/${MAIN_URL:?}.cert.pem /home/export/${MAIN_URL:?}.cert.key.pem
