#!/bin/bash

readonly MAIN_URL="djuxt.local"
readonly CRT_EXT=".crt"
readonly KEY_EXT=".key"
readonly CSR_EXT=".csr"

cd /root/ca/ && \

openssl genrsa -aes256 -out private/ca${KEY_EXT:?} 4096 && \

chmod 400 private/ca${KEY_EXT:?} && \

openssl req -config openssl.cnf \
      -key private/ca${KEY_EXT:?} \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca${CRT_EXT:?} && \

chmod 444 certs/ca${CRT_EXT:?} && \

openssl x509 -noout -text -in certs/ca${CRT_EXT:?} && \

cp /root/ca/certs/ca${CRT_EXT:?} /home/export/