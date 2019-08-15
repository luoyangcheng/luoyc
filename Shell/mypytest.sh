#!/bin/bash
export PATH=/usr/local/bin:$PATH
cd /data/luoyc/TheFame
chmod 777 /data/luoyc/TheFame/logs/
python -m pytest --html=report.html