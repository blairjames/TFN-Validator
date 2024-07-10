#!/usr/bin/env bash

main() {
  sudo docker build -t docker.io/blairy/tfn-validator . || exit 1
  sudo docker push docker.io/blairy/tfn-validator || exit 1
  curl -X POST https://hub.docker.com/api/build/v1/source/222a93ce-2bc4-425b-9c45-473f589d8e22/trigger/760b3256-9bde-4821-96ff-3e1daa09309a/call/ || exit 1
}

main
