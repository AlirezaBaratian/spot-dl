#!/usr/bin/env bash

function main() {
    echo "YOU NEED TO CREATE .env FIRST!"
    sleep 3

    # Install pip and the dependencies
    apt update
    apt install -y python3-pip
    pip install -r requirements.txt

    # Deploy
    pm2 start main.py --interpreter python3
}

main
