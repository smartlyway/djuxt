FROM nginx:latest
COPY conf/nginx-ssl.conf /etc/nginx/nginx.conf
COPY conf/uwsgi_params /home/docker/code/

COPY  certs/api.djuxt.local.cert.pem /etc/ssl/certs/api.djuxt.local.cert.pem
COPY  certs/api.djuxt.local.no-key.pem /etc/ssl/private/api.djuxt.local.key.pem
COPY  certs/djuxt.local.cert.pem /etc/ssl/certs/djuxt.local.cert.pem
COPY  certs/djuxt.local.no-key.pem /etc/ssl/private/djuxt.local.key.pem

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]