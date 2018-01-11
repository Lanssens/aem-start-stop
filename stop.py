#!/usr/bin/python
import os

# Path to bin folder
authorpath = "~/Desktop/aem/author/crx-quickstart/bin"
publishpath = "~/Desktop/aem/publish/crx-quickstart/bin"
activemqpath = "~/Documents/apache-activemq-5.15.1/bin"

# Stop author 
os.system("sh " + authorpath + "/stop")

# Stop publisher
os.system("sh " + publishpath + "/stop")

# Stop activeMQ
os.system( activemqpath + "/activemq stop")