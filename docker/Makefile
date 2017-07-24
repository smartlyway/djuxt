#===============================================================================
#    _____             _       _____ _      _____
#   |  __ \           | |     / ____| |    |_   _|
#   | |  | | ___   ___| | __ | |    | |      | |
#   | |  | |/ _ \ / __| |/ / | |    | |      | |
#   | |__| | (_) | (__|   <  | |____| |____ _| |_
#   |_____/ \___/ \___|_|\_\  \_____|______|_____|
#
#===============================================================================

#===============================================================================
#   BUILD
#===============================================================================
b:
	docker-compose build nginx django postgres mongo node

b-django:
	docker-compose build django

b-nginx:
	docker-compose build nginx

b-nginx-test:
	docker-compose build nginx
	docker-compose up -d nginx
	docker-compose exec nginx nginx -t -c /etc/nginx/sites-available/default

#===============================================================================
#   UP
#===============================================================================
u:
	docker-compose up -d nginx django postgres mongo node

u-node:
	docker-compose up -d node

uc-node:
	docker-compose up node

u-nginx:
	docker-compose up -d nginx

uc-nginx:
	docker-compose up nginx

u-django:
	docker-compose up -d django

uc-django:
	docker-compose up django

#===============================================================================
#  DOWN
#===============================================================================
d:
	docker-compose down

#===============================================================================
#   SHELLS
#===============================================================================
s-django:
	docker-compose exec django bash

s-node:
	docker-compose exec node bash

s-nginx:
	docker-compose exec nginx bash

s-nginx-test:
	docker-compose exec nginx nginx -t -c /etc/nginx/sites-available/default

#===============================================================================
#   RESTART
#===============================================================================
r-all:
	docker-compose down
	docker-compose up -d django postgres mongo node

r-nginx:
	docker-compose build nginx
	docker-compose up -d nginx

r-django:
	docker-compose restart django

#===============================================================================
#   GLOBAL
#===============================================================================
g-remove-all:
	docker stop $(docker ps -a -q)

g-stop-all:
	docker rm $(docker ps -a -q)

#===============================================================================
#   NEW
#===============================================================================
n-project:
	docker-compose exec django django-admin.py startproject config /home/docker/code/app/

#===============================================================================
#   DJANGO
#===============================================================================
dj-ngix:
	docker-compose build django
	docker-compose up django

dj-man-migrate:
	docker-compose exec django python3 manage.py makemigrations
	docker-compose exec django python3 manage.py migrate

dj-man-collectstatic:
	docker-compose exec django python3 manage.py collectstatic