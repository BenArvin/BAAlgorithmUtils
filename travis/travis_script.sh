#!/bin/bash

#remove last build packages
sudo rm -rf /dist/*

#build new packages
sudo python3 setup.py sdist bdist_wheel