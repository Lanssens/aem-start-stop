#!/usr/bin/env python

''' 
python-tail example.
Does a tail follow against /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines to standard out '''

import tail

def print_line(txt):
    ''' Prints received text '''
    print(txt)

t = tail.Tail('~/Documents/projects/vo/aem/publish/crx-quickstart/logs/error.log')
t.register_callback(print_line)
t.follow(s=5)


