#!/bin/bash

readonly MAIN_URL="djuxt.local"
readonly CRT_EXT=".crt"
readonly KEY_EXT=".key"
readonly CSR_EXT=".csr"

cd /root/ca && \

#   CREATE A KEY
#-------------------------------------------------------------------------
openssl genrsa \
        -aes256 \
        -out intermediate/private/${MAIN_URL:?}${KEY_EXT:?} 2048  && \

chmod 400 intermediate/private/${MAIN_URL:?}${KEY_EXT:?}   && \

#   CREATE A CERTIFICATE
#-------------------------------------------------------------------------
openssl req \
        -config intermediate/web-openssl.cnf \
        -key intermediate/private/${MAIN_URL:?}${KEY_EXT:?} \
        -new -sha256 -out intermediate/csr/${MAIN_URL:?}${CSR_EXT:?} && \

#   SIGN CERTIFICATE
#-------------------------------------------------------------------------
openssl ca \
        -config intermediate/web-openssl.cnf \
        -extensions server_cert -days 375 -notext -md sha256 \
        -in intermediate/csr/${MAIN_URL:?}${CSR_EXT:?} \
        -out intermediate/certs/${MAIN_URL:?}${CRT_EXT:?} && \

chmod 444 intermediate/certs/${MAIN_URL:?}${CRT_EXT:?} && \

#   DELETE PASSWORD FOR NGINX USAGE
#-------------------------------------------------------------------------
openssl rsa \
        -in /root/ca/intermediate/private/${MAIN_URL:?}${KEY_EXT:?} \
        -out /root/ca/intermediate/private/${MAIN_URL:?}.no-pass${KEY_EXT:?} \

cp /root/ca/intermediate/certs/${MAIN_URL:?}${CRT_EXT:?} /home/export/ && \
cp /root/ca/intermediate/certs/${MAIN_URL:?}${KEY_EXT:?} /home/export/ && \
cp /root/ca/intermediate/certs/${MAIN_URL:?}${MAIN_URL:?}.no-pass.${KEY_EXT:?} /home/export/
