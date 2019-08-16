#!/bin/bash
export PATH=/usr/local/bin:$PATH
chmod 777 -R /data/luoyc/TheFame/
cd /data/luoyc/TheFame
python -m pytest --html=report.html