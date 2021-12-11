FROM python:3.7

# Create a directory named flask
RUN mkdir app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy everything to flask folder
COPY . /app/

# Make flask as working directory
WORKDIR /app

# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]