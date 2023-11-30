#!/bin/bash
# Get the byte size in a response for a given URL.
curl -s "$1" | wc -c
