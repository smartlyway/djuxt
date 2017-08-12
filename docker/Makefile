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
	docker-compose build nginx django postgres mongo node-nuxt node-angular

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
	docker-compose up -d django node-nuxt nginx postgres mongo
	sleep 5
	docker-compose up -d nginx

u-node-nuxt:
	docker-compose up -d node-nuxt

u-node-angular:
	docker-compose up -d node-angular

u-nginx:
	docker-compose up -d nginx

u-django:
	docker-compose up -d django

#===============================================================================
#   UP with console
#===============================================================================
uc-django:
	docker-compose up django
	
uc-nginx:
	docker-compose up nginx

uc-node-nuxt:
	docker-compose up node-nuxt

uc-node-angular:
	docker-compose up node-angular

#===============================================================================
#  DOWN
#===============================================================================
d:
	docker-compose down

l-django:
	docker-compose exec django bash -c "cd ../logs && cat uwsgi-err.log"
#===============================================================================
#   SHELLS
#===============================================================================
s-django:
	docker-compose exec django bash

s-node-nuxt:
	docker-compose exec node-nuxt bash

s-node-angular:
	docker-compose exec node-angular bash

s-nginx:
	docker-compose exec nginx bash

s-nginx-test:
	docker-compose exec nginx nginx -t -c /etc/nginx/sites-available/default

#===============================================================================
#   RESTART
#===============================================================================
r-all:
	docker-compose down
	docker-compose up -d django postgres mongo node-nuxt

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