#!/usr/bin/env python

import tail
import os
import sys

# Path to instance folder
authorpath = os.getenv('AUTHOR_PATH')
publishpath = os.getenv('PUBLISH_PATH')

def print_line(txt):
    ''' Prints received text '''
    print(txt),

print(sys.argv[1])    

if (sys.argv[1] and sys.argv[1] == 'author' and authorpath is not None):
	print("Opened author error log")

	concatted_path = authorpath + "/crx-quickstart/logs/error.log"
	print(concatted_path)
	t = tail.Tail(os.path.expanduser(concatted_path)) 
	t.register_callback(print_line)
	t.follow(s=2)

elif (sys.argv[1] and sys.argv[1] == 'publish' and publishpath is not None):
	print("Opened publish error log")

	concatted_path = publishpath + "/crx-quickstart/logs/error.log"
	print(concatted_path)
	t = tail.Tail(os.path.expanduser(concatted_path)) 
	t.register_callback(print_line)
	t.follow(s=2)