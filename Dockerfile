FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

RUN apk add --update \
    build-base \
    jpeg-dev \
    zlib-dev \
    postgresql-dev \
    gettext \
    bash \
    zip \
    unzip \
    git \
	nano \
	vim

ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE website.settings.docker

COPY requirements.txt .

RUN pip install -r requirements.txt && \
    pip install gunicorn

COPY . .

RUN git clone https://github.com/oznakn/docker-scripts && \
  	mv docker-scripts/*.sh . && \
  	rm -rf docker-scripts && \
	mkdir -p ./db

RUN chmod a+x backup-data.sh restore-data.sh docker-wait-for-it.sh
