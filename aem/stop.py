#!/usr/bin/python
import os

# Path to bin folder
authorpath = os.getenv('AUTHOR_PATH')
publishpath = os.getenv('PUBLISH_PATH')
activemqpath = os.getenv('ACTIVEMQ_PATH')

# Stop author 
if authorpath!="None":
	os.system("sh " + authorpath + "/crx-quickstart/bin/stop")

# Stop publisher
if publishpath!="None": 
	os.system("sh " + publishpath + "/crx-quickstart/bin/stop")

# Stop activeMQ
if activemqpath!="None":
	os.system( activemqpath + "/bin/activemq stop")

print 'Stopped services'