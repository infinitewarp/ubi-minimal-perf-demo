Demonstration of UBI9 performance regression compared with UBI8.

## Build

```sh
docker build -t ubi-minimal-perf-demo:ubi8 -f Dockerfile_ubi8 .
docker build -t ubi-minimal-perf-demo:ubi9 -f Dockerfile_ubi9 .
```

## Set environment variables

You must have access keys for an AWS account, and those keys must have the ability to write to CloudWatch.

```sh
# enter your AWS access key id and secret access key.
# these are required for watchtower to send logs to AWS cloudwatch.
read -s CLOUDWATCH_AWS_ACCESS_KEY_ID
read -s CLOUDWATCH_AWS_SECRET_ACCESS_KEY

# optional env variables; code assumes these defaults if not set.
# CLOUDWATCH_AWS_REGION_NAME="us-east-1"
# CLOUDWATCH_LOG_GROUP="demo-log-group"
# CLOUDWATCH_LOG_STREAM_NAME="demo-log-stream"
# LOG_LEVEL="INFO"
# DJANGO_LOG_LEVEL="ERROR"
```

## Benchmark UBI8

```sh
# run the demo server on ubi8.
# add extra env variables with -e as needed.
CONTAINER_ID=$(docker run -d --rm \
    -p 8000:8000 \
    -e "CLOUDWATCH_AWS_ACCESS_KEY_ID=${CLOUDWATCH_AWS_ACCESS_KEY_ID}" \
    -e "CLOUDWATCH_AWS_SECRET_ACCESS_KEY=${CLOUDWATCH_AWS_SECRET_ACCESS_KEY}" \
    ubi-minimal-perf-demo:ubi8)

# verify ther container is running.
docker ps -f "id=${CONTAINER_ID}"

# run ab (apache bench) with a moderate number of requests.
# capture the output if you wish.
ab -c2 -n200 http://127.0.0.1:8000/ 2>&1 | tee /tmp/ubi8-demo-ab.txt

# save the container logs if you wish.
docker logs "${CONTAINER_ID}" > /tmp/ubi8-demo-logs.txt 2>&1

# kill the container
docker kill "${CONTAINER_ID}"
```

## Benchmark UBI9

Same as above instructions for UBI8, but `s/ubi8/ubi9/g`.

```sh
# run the demo server on ubi9.
# add extra env variables with -e as needed.
CONTAINER_ID=$(docker run -d --rm \
    -p 8000:8000 \
    -e "CLOUDWATCH_AWS_ACCESS_KEY_ID=${CLOUDWATCH_AWS_ACCESS_KEY_ID}" \
    -e "CLOUDWATCH_AWS_SECRET_ACCESS_KEY=${CLOUDWATCH_AWS_SECRET_ACCESS_KEY}" \
    ubi-minimal-perf-demo:ubi9)

# verify ther container is running.
docker ps -f "id=${CONTAINER_ID}"

# run ab (apache bench) with a moderate number of requests.
# capture the output if you wish.
ab -c2 -n200 http://127.0.0.1:8000/ 2>&1 | tee /tmp/ubi9-demo-ab.txt

# save the container logs if you wish.
docker logs "${CONTAINER_ID}" > /tmp/ubi9-demo-logs.txt 2>&1

# kill the container
docker kill "${CONTAINER_ID}"
```
