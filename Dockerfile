# syntax = docker/dockerfile:experimental
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# python3 and all dependencies for scipy
RUN apt update && apt install -y liboctave-dev octave octave-control python3 python3-pip libatlas-base-dev libfreetype6-dev

# Update pip
RUN pip3 install -U pip==22.0.3

# Cython and scikit-learn - it needs to be done in this order for some reason
RUN pip3 --no-cache-dir install Cython==0.29.24

# Rest of the dependencies
COPY requirements-blocks.txt ./
RUN pip3 --no-cache-dir install -r requirements-blocks.txt

COPY third_party /third_party
COPY . ./

# Install Octave dependencies
RUN octave setup.m

EXPOSE 4446

ENTRYPOINT ["python3", "-u", "dsp-server.py"]
