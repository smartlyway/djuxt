FROM ubuntu:16.04

MAINTAINER Dockerfiles

#-------------------------------------------------------------------------------
# Install required packages and remove the apt packages cache when done.
#-------------------------------------------------------------------------------
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	openssl

#-------------------------------------------------------------------------------
# Create folders and set permissions
#-------------------------------------------------------------------------------

#   ROOT CA
#-----------------------------------------------------
RUN mkdir -p /root/ca/ && \
    cd /root/ca && \
    mkdir certs crl newcerts private && \
    chmod 700 private && \
    touch index.txt  && \
    echo 1000 > serial

COPY conf/root-openssl.cnf /root/ca/openssl.cnf

#   INTERMEDIATE CA
#-----------------------------------------------------
RUN mkdir /root/ca/intermediate && \
    cd /root/ca/intermediate && \
    mkdir certs crl csr newcerts private && \
    chmod 700 private && \
    touch index.txt && \
    echo 1000 > serial && \
    echo 1000 > /root/ca/intermediate/crlnumber

COPY conf/intermediate-openssl.cnf /root/ca/intermediate/openssl.cnf

#   WEB CONFIG
#-----------------------------------------------------
COPY conf/web-openssl.cnf /root/ca/intermediate/web-openssl.cnf


COPY scripts/* /home/

WORKDIR /home/

CMD exec /bin/bash -c "trap : TERM INT; sleep 500000 & wait"

