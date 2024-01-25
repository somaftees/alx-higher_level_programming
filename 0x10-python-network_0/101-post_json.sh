#!/bin/bash
# a Bash script that sends a JSON
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
