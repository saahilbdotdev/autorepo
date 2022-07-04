#!/bin/bash

echo "Uninstalling..."

sudo rm -rf /opt/autorepo
sudo rm -f /usr/local/bin/repo
rm -rf $HOME/.config/autorepo

echo "AutoRepo has been uninstalled."
