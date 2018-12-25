FROM python:3.6-alpine

RUN apk add --update build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD sh -c "python manage.py migrate && \
        python manage.py collectstatic --no-input && \
        ./restore-data.sh db.zip && \
		python3 manage.py runserver 0.0.0.0:8000"