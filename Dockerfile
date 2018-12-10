FROM python:3.6-jessie

COPY core/ /opt
COPY requirement.txt /opt

WORKDIR /opt
RUN apt-get update && apt-get install -y nginx
RUN pip3 install gunicorn
RUN pip3 install -r requirement.txt

ENV PRODUCTION=true

COPY deploy/nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

EXPOSE 8080

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
