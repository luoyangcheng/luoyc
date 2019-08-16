#!/bin/bash
export PATH=/usr/local/bin:$PATH
chmod -R 777 /data/luoyc/TheFame/
cd /data/luoyc/TheFame
python -m pytest --html=report.html