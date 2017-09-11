FROM nginx:latest
COPY conf/nginx-ssl.conf /etc/nginx/nginx.conf
COPY conf/uwsgi_params /home/docker/code/

COPY  certs/djuxt.local.crt /etc/ssl/certs/
COPY  certs/djuxt.local.no-pass.key /etc/ssl/private/


STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]