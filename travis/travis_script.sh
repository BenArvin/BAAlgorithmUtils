#!/bin/bash

#remove last build result
sudo rm -rf /build/*
sudo rm -rf /dist/*

#build new packages
sudo python3 setup.py sdist bdist_wheel