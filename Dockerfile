FROM python:3.11-alpine AS builder

WORKDIR /app


RUN apk add --no-cache \
    build-base \
    jpeg-dev \
    zlib-dev \
    postgresql-dev \
    gcc \
    musl-dev \
    python3-dev

COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir gunicorn && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.11-alpine

WORKDIR /app


RUN apk add --no-cache \
    libpq \
    jpeg-dev \
    zlib-dev \
    gettext \
    bash


COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*


COPY . .


RUN git clone https://github.com/metucclub/docker-scripts && \
    mv docker-scripts/*.sh . && \
    rm -rf docker-scripts && \
    mkdir -p ./db && \
    chmod a+x *.sh

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE website.settings.docker
