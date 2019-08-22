#!/bin/bash

ACTION=$1
IMAGE="mandelbot/sarima"

if [[ -z $ACTION ]]; then
    echo "Usage: mandelbot_sarima.sh [build/run]"
    exit 1
fi

if [[ $ACTION = 'build' ]];
then
    echo "Building Docker image: $IMAGE"
    docker build . -t $IMAGE
elif [[ $ACTION = 'run' ]];
then
    echo "Running flask"
    docker run -p 8888:8888 -it $IMAGE
else
    echo "Usage: mandelbot_sarima.sh [build/run]"
fi