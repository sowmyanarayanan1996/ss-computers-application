FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /services

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN python -m pip install --upgrade pip
RUN pip install psycopg2-binary

USER root

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /services/


