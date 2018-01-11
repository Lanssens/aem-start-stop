#!/usr/bin/python
import os

# Path to bin folder
authorpath = os.getenv('AUTHOR_BIN_PATH')
publishpath = os.getenv('PUBLISH_BIN_PATH')
activemqpath = os.getenv('ACTIVEMQ_BIN_PATH')

# Start author 
os.system("sh " + authorpath + "/start")

# Start publisher
os.system("sh " + publishpath + "/start")

# Start activeMQ
os.system( activemqpath + "/activemq start")