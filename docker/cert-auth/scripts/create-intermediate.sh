#!/bin/bash

readonly CRT_EXT=".crt"
readonly KEY_EXT=".key"
readonly CSR_EXT=".csr"

cd /root/ca && \

openssl genrsa -aes256 \
      -out intermediate/private/intermediate${KEY_EXT:?} 4096 && \

chmod 400 intermediate/private/intermediate${KEY_EXT:?} && \

openssl req -config intermediate/openssl.cnf -new -sha256 \
      -key intermediate/private/intermediate${KEY_EXT:?} \
      -out intermediate/csr/intermediate${CSR_EXT:?} && \

openssl ca -config openssl.cnf -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in intermediate/csr/intermediate${CSR_EXT:?} \
      -out intermediate/certs/intermediate${CRT_EXT:?}  && \

chmod 444 intermediate/certs/intermediate${CRT_EXT:?} && \

cat intermediate/certs/intermediate${CRT_EXT:?} \
      certs/ca${CRT_EXT:?} > intermediate/certs/ca-chain${CRT_EXT:?} && \

chmod 444 intermediate/certs/ca-chain${CRT_EXT:?} && \

cp /root/ca/intermediate/certs/intermediate${CRT_EXT:?} /home/export/