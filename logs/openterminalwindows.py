#!/usr/bin/env python

import tail
import os
import time

os.system("python terminal.py --wait python followerrorlog.py author")

time.sleep(1)

os.system("python terminal.py --wait python followerrorlog.py publish")