#!/bin/bash
export PATH=/usr/local/bin:$PATH
cd /data/luoyc
git stash
{git pull origin master} || {rm -rf ./TheFame/logs ./TheFame/.pytest_cache ./TheFame/__pycache__ ./TheFame/case}&& git pull origin master
