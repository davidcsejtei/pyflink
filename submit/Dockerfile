FROM apache/flink:1.17.1-scala_2.12

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip netcat && \
    pip3 install apache-flink==1.17.1

ENV PYFLINK_PYTHON_EXECUTABLE=python3

WORKDIR /opt
COPY wait-for-jobmanager.sh .
RUN chmod +x wait-for-jobmanager.sh

USER flink