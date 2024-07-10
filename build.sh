#!/usr/bin/env bash

main() {
  sudo docker build -t tfn-validator . || exit 1
}

main