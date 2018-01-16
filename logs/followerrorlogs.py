#!/usr/bin/env python

''' 
python-tail example.
Does a tail follow against /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines to standard out '''

import tail
import os

# Path to bin folder
authorpath = os.getenv('AUTHOR_PATH')

def print_line(txt):
    ''' Prints received text '''
    print(txt)

if authorpath!="None":
	os.system("python terminal.py --wait ls -la")
	os.system("python terminal.py --wait ls -la")
	
	concatted_path = authorpath + "/crx-quickstart/logs/error.log"
	print(concatted_path)
	t = tail.Tail(os.path.expanduser(concatted_path)) 
	t.register_callback(print_line)
	t.follow(s=5)