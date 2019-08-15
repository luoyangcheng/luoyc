#!/bin/bash
export PATH=/usr/local/bin:$PATH
chmod 777 /data/luoyc/TheFame/logs/
cd /data/luoyc/TheFame
python -m pytest --html=report.html