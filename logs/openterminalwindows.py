#!/usr/bin/env python

import tail
import os
import time

repopath = os.getenv('REPO_PATH')
 
os.system("python " + repopath + "/logs/terminal.py --wait python " + repopath + "/logs/followerrorlog.py author")

time.sleep(1)

os.system("python " + repopath + "/logs/terminal.py --wait python " + repopath + "/logs/followerrorlog.py publish")