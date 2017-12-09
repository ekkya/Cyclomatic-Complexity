import platform

profile = [
platform.architecture(),
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),
platform.machine(),
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
platform.uname(),
platform.version(),
]

for item in profile:
  print itemimport os
home=os.path.expanduser("~")
print home
if not os.path.exists(home+'/testdir'):
  os.makedirs(home+'/testdir')# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

import subprocess								# Import the subprocess module
for server in open('server_list.txt'):		# Open the file and read each line
	subprocess.Popen(('nslookup '+server))	# Run the nslookup command for each server in the list# Script Name		: testlines.py
# Author				: Craig Richards
# Created				: 08th December 2011
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This very simple script open a file and prints out 100 lines of whatever is set for the line variable

line="Test you want to print\n"	# This sets the variable for the text that you want to print
f=open('mylines.txt','w')				# Create the file to store the output
for i in range(1,101):					# Loop 100 times
  f.write(line)								# Write the text to the file
f.close()									# Close the file# Script Name		: ping_subnet.py
# Author				: Craig Richards
# Created				: 12th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: After supplying the first 3 octets it will scan the final range for available addresses

import os				# Load the Library Module
import subprocess	# Load the Library Module 
import sys				# Load the Library Module

filename = sys.argv[0]	# Sets a variable for the script name

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:	# Help Menu if called
    print '''
You need to supply the first octets of the address Usage : ''' + filename + ''' 111.111.111 '''
    sys.exit(0)
else:

	if (len(sys.argv) < 2): # If no arguments are passed then display the help and instructions on how to run the script
		sys.exit (' You need to supply the first octets of the address Usage : ' + filename + ' 111.111.111')

	subnet = sys.argv[1]	# Set the variable subnet as the three octets you pass it
	
	if os.name == "posix":	# Check the os, if it's linux then			
		myping = "ping -c 2 "	# This is the ping command
	elif os.name in ("nt", "dos", "ce"):	# Check the os, if it's windows then
		myping = "ping -n 2 "	# This is the ping command

	f = open('ping_'+subnet+'.log', 'w')	# Open a logfile
	for ip in range(2,255):	# Set the ip variable for the range of numbers
		ret = subprocess.call(myping + str(subnet)+"."+str(ip) , shell=True,stdout=f,stderr=subprocess.STDOUT) # Run the command pinging the servers
		if ret == 0:	# Depending on the response
			f.write (subnet+"."+str(ip) + " is alive" + "\n")	# Write out that you can receive a reponse
		else: 
			f.write (subnet+"."+str(ip) + " did not respond" + "\n")	# Write out you can't reach the box# Script Name		: dir_test.py
# Author				: Craig Richards
# Created				: 29th November 2011
# Version				: 1.0

# Modifications		: 
# Description			: Tests to see if the directory testdir exists, if not it will create the directory for you

import os									# Import the OS module

if not os.path.exists('testdir'):		#  Check to see if it exists
  os.makedirs('testdir')				#  Create the directory