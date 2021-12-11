FROM python:3.7

# Create a directory named flask
RUN mkdir app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat && apt-get -y install cron

# Copy everything to flask folder
COPY . /app/

# Make flask as working directory
WORKDIR /app

# Install the Python libraries
# RUN pip3 install --no-cache-dir -r requirements.txt
# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

RUN chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]