FROM arm32v7/ubuntu:16.04

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
	supervisor && \
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

#-------------------------------------------------------------------------------
# COPY configuration files
#-------------------------------------------------------------------------------
COPY conf/uwsgi.ini /home/docker/code/

WORKDIR /home/docker/code/app/
RUN mkdir /home/docker/code/logs
#-------------------------------------------------------------------------------
# EXPOSE Http and Https ports
#-------------------------------------------------------------------------------
CMD ["uwsgi", "--ini" ,"/home/docker/code/uwsgi.ini"]