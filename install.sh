#!/bin/bash

echo "Starting installation..."

pip install -r requirements.txt

sudo mkdir -p /opt/autorepo
sudo chown -R $USER:$USER /opt/autorepo

mkdir -p $HOME/.config/autorepo

sudo cp -r ./utils /opt/autorepo
sudo cp ./main.py /opt/autorepo/repo
sudo chmod +x /opt/autorepo/repo

sudo ln -s /opt/autorepo/repo /usr/local/bin/repo

echo "Installation completed successfully!"
