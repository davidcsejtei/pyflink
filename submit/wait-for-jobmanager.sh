#!/bin/bash
echo "Waiting for Flink JobManager at jobmanager:8081..."
while ! nc -z jobmanager 8081; do
  sleep 1
done
echo "JobManager is up. Submitting job..."