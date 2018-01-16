#!/usr/bin/python
import os

# Path to bin folder
authorpath = os.getenv('AUTHOR_PATH')
publishpath = os.getenv('PUBLISH_PATH')
activemqpath = os.getenv('ACTIVEMQ_PATH')

# Start author 
if authorpath!="None":
	os.system("sh " + authorpath + "/crx-quickstart/bin/start")

# Start publisher
if publishpath!="None":
	os.system("sh " + publishpath + "/crx-quickstart/bin/start")

# Start activeMQ
if activemqpath!="None":
	os.system( activemqpath + "/bin/activemq start")

print 'Done starting services'