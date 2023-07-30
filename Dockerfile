FROM python:3.8

WORKDIR /app
# ADD main.py /
EXPOSE 8000
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./app /app
COPY ./data /data
RUN apt-get update && apt-get install -y postgresql-client

