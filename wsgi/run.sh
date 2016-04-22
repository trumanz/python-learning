#!/bin/sh
./server.py & sleep 1
version=$(curl localhost:8080)

echo $version

