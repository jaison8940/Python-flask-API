FROM alpine:latest

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk add py3-greenlet
RUN apk add g++
RUN apk add curl
RUN pip install --upgrade pip


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]