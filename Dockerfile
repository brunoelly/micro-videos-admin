FROM python:3.10.2-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jre git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

CMD [ "tail", "-f", "/dev/null" ]

ENV PYTHONPATH=${PYTHONPATH}/home/python/app
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64