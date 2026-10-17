FROM python:3.11-slim

#Environmental Variables
ENV PYHTONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Copy to and set working directory
WORKDIR /app
COPY . /app


#Install Backend Requirements
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config 
COPY ./am_framework/requirements.txt /app/
RUN pip install -r requirements.txt