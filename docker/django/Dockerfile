FROM ubuntu:16.04

MAINTAINER Dockerfiles

#-------------------------------------------------------------------------------
# Install required packages and remove the apt packages cache when done.
#-------------------------------------------------------------------------------
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

#-------------------------------------------------------------------------------
# Install uWSGI (it takes a liltle while)
#-------------------------------------------------------------------------------
RUN pip3 install uwsgi

#-------------------------------------------------------------------------------
# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code,
# this will cause Docker's caching mechanism to prevent re-installing (all your)
# dependencies when you made a change a line or two in your app.
#-------------------------------------------------------------------------------
COPY app/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

#CREATE SSL SELF SIGNED
RUN mkdir /opt/ssl
COPY conf/self-signed-cert.cnf /opt/ssl
RUN cd /opt/ssl/ && \
	openssl genrsa -des3 -passout pass:x -out server.pass.key 2048 && \
	openssl rsa -passin pass:x -in server.pass.key -out server.key && \
	rm server.pass.key && \
	openssl req -new -key server.key -out server.csr -config self-signed-cert.cnf -subj "/" && \
	openssl x509 -req -sha256 -days 300065 -extfile self-signed-cert.cnf -in server.csr -signkey server.key -out server.crt

#-------------------------------------------------------------------------------
# COPY configuration files
#-------------------------------------------------------------------------------
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY conf/nginx-app.conf /etc/nginx/sites-available/default
COPY conf/supervisor-app.conf /etc/supervisor/conf.d/
COPY conf/* /home/docker/code/

WORKDIR /home/docker/code/app/

#-------------------------------------------------------------------------------
# EXPOSE Http and Https ports
#-------------------------------------------------------------------------------
EXPOSE 80 443

CMD ["supervisord", "-n"]