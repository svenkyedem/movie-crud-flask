#!/bin/sh
set +e
SRC_DIRECTORY="$(pwd)"
REPORT_DIRECTORY="$SRC_DIRECTORY/report"

if [ ! -d "$REPORT_DIRECTORY" ]; then
    echo "Initially creating persistent directories"
    mkdir -p "$REPORT_DIRECTORY"
    chmod -R 777 "$REPORT_DIRECTORY"
fi

# Make sure we are using the latest version
docker pull secfigo/bandit:latest

docker run --rm \
    --volume $(pwd):/src \
    --volume "$REPORT_DIRECTORY":/report \
    secfigo/bandit:latest
