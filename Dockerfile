FROM python:3.10-slim

WORKDIR /app

# set environment variables
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Install system dependencies
# Setup GDAL
# Install system dependencies
# Setup GDAL
# RUN apt-get update &&\
#    apt-get install -y binutils libproj-dev  gdal-bin libgdal-dev  libgeos-dev python3-gdal \
#    && apt-get clean
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y libgeos++-dev \
    && apt-get install -y proj-bin \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev \
    && apt-get clean


# Ensure libgdal version matches the GDAL Python bindings

ENV GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgdal.so

COPY . /app

# upgrade pip version
RUN pip install --upgrade pip \
   && chmod +x docker-entrypoint.sh

# copy requirements to the image
COPY ./requirements.txt /app/requirements.txt

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt




# Expose port
EXPOSE 8000