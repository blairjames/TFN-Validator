#!/usr/bin/env bash

main() {
 sudo docker run --rm -it docker.io/blairy/tfn-validator || exit 1
}

main
