# aem-start-stop
Python scripts that starts and stops AEM ( and my project specific services )

## Installation
You need to have python2 installed

	brew install python
	
## How to use

Set the following environment variables in .bash_profile: 

	export AUTHOR_BIN_PATH=<author_bin_path> 
	export PUBLISH_BIN_PATH=<publish_bin_path>
	(export ACTIVEMQ_BIN_PATH=<activemq_bin_path>) --> optional

The scripts will pick up the environment variables and will start the services that have valid paths.

Make aliases for start.py and stop.py to make your life easier:
	
	alias startaem='python <path_to_start.py>' 
	alias stopaem='python <path_to_stop.py>' 
		
Refresh the shell environment for everything to work: 
		
	source ~/.bash_profile

Finally: 
		
	startaem
		...
	stopaem
		...