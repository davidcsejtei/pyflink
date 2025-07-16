FROM apache/flink:1.17.1-scala_2.12

USER root

# Telepítsük a python3-at és pip-et
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install apache-flink==1.17.1

# Állítsuk be az interpretert, ha a PyFlink explicit használja
ENV PYFLINK_PYTHON_EXECUTABLE=python3