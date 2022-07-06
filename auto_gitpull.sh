#!/bin/bash

sleep 10
now=$(date +"%T")
echo "Attempting to git pull at : $now"
cd Brake_Press/
sudo git pull --rebase
sudo chmod +x PressDisplay3.py
sudo chmod +x auto_gitpull.sh

