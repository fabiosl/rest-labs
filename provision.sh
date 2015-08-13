#!/bin/bash

echo "Start VM provisioning..."

sudo apt-get update

# Tools
sudo apt-get install -y python-pip

# Python Libraries
sudo pip install Flask
