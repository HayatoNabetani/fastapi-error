FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y default-mysql-client \
    && apt-get -y install gcc libmariadb-dev \
    && apt-get install --no-install-recommends -y tzdata \
    && apt-get -y install wkhtmltopdf \
    && apt-get -y install unzip \
    && apt-get -y install fontconfig \
    && apt-get -y install unixodbc \
    && apt-get clean

ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone

WORKDIR /workspace
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

