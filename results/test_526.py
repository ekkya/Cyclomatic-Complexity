# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

import subprocess								# Import the subprocess module
for server in open('server_list.txt'):		# Open the file and read each line
	subprocess.Popen(('nslookup '+server))	# Run the nslookup command for each server in the list# Script Name		: dir_test.py
# Author				: Craig Richards
# Created				: 29th November 2011
# Version				: 1.0

# Modifications		: 
# Description			: Tests to see if the directory testdir exists, if not it will create the directory for you

import os									# Import the OS module

if not os.path.exists('testdir'):		#  Check to see if it exists
  os.makedirs('testdir')				#  Create the directory