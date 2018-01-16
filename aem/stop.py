#!/usr/bin/python
import os

# Path to instance folder
authorpath = os.getenv('AUTHOR_PATH')
publishpath = os.getenv('PUBLISH_PATH')
activemqpath = os.getenv('ACTIVEMQ_PATH')

# Stop author 
if authorpath is not None:
	os.system("sh " + authorpath + "/crx-quickstart/bin/stop")

# Stop publisher
if publishpath is not None: 
	os.system("sh " + publishpath + "/crx-quickstart/bin/stop")

# Stop activeMQ
if activemqpath is not None:
	os.system( activemqpath + "/bin/activemq stop")

print 'Stopped services'