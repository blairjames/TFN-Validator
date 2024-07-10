#!/usr/bin/env bash

main() {
 sudo docker run --rm -it tfn-validator || exit 1
}

main