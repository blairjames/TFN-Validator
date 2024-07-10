#!/usr/bin/env bash

main() {
  sudo docker build -t docker.io/blairy/tfn-validator . || exit 1
}

main
