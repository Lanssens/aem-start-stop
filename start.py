#!/usr/bin/python
import os

# Path to bin folder
authorpath = os.getenv('KEY_THAT_MIGHT_EXIST')
publishpath = os.getenv('KEY_THAT_MIGHT_EXIST')
activemqpath = os.getenv('KEY_THAT_MIGHT_EXIST')

# Start author 
os.system("sh " + authorpath + "/start")

# Start publisher
os.system("sh " + publishpath + "/start")

# Start activeMQ
os.system( activemqpath + "/activemq start")