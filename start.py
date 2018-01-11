#!/usr/bin/python
import os

# Path to bin folder
authorpath = "~/Desktop/aem/author/crx-quickstart/bin"
publishpath = "~/Desktop/aem/publish/crx-quickstart/bin"
activemqpath = "~/Documents/apache-activemq-5.15.1/bin"

# Start author 
os.system("sh " + authorpath + "/start")

# Start publisher
os.system("sh " + publishpath + "/start")

# Start activeMQ
os.system( activemqpath + "/activemq start")