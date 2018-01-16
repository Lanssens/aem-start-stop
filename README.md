# aem-start-stop
Python scripts that starts and stops AEM. You can also open both the error logs of publisher and author with a single command.

## Installation
You need to have python2 installed

	brew install python
	
## How to use

Set the following environment variables in .bash_profile: 

	export AUTHOR_PATH=<author_path> 
	export PUBLISH_PATH=<publish_path>
	export REPO_PATH=<repo_path>
	(export ACTIVEMQ_PATH=<activemq_path>) --> optional

The scripts will pick up the environment variables and will start the services that have valid paths.

Make aliases for start.py, stop.py and openterminalwindows.py to make your life easier. Put them in .bash_profile/.zshrc/...:
	
	alias startaem='python <repo/aem/start.py>' 
	alias stopaem='python <repo/aem/stop.py>' 
	alias openerrorlogs='python <repo/logs/openterminalwindows.py>'
		
Refresh your shell environment for everything to work: 
		
	source ~/.bash_profile

Finally: 
		
	startaem
		...
	stopaem
		...	
	openerrorlogs
		...