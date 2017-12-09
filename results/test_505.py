# Script Name		: osinfo.py
# Author				: Craig Richards
# Created				: 5th April 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: Displays some information about the OS you are running this script on

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
  print item# Script Name		: logs.py
# Author				: Craig Richards
# Created				: 13th October 2011
# Last Modified		: 
# Version				: 1.1
# Modifications		: 1.1 - Added the variable zip_program so you can set it for the zip program on whichever OS, so to run on a different OS just change the locations of these two variables.

# Description			: This script will search for all *.log files in the given directory, zip them using the program you specify and then date stamp them

import os																	# Load the Library Module
from time import strftime												# Load just the strftime Module from Time

logsdir="c:\puttylogs"													# Set the Variable logsdir
zip_program="zip.exe"												# Set the Variable zip_program - 1.1

for files in os.listdir(logsdir):										# Find all the files in the directory
	if files.endswith(".log"):											# Check to ensure the files in the directory end in .log
		files1=files+"."+strftime("%Y-%m-%d")+".zip"		# Create the Variable files1, this is the files in the directory, then we add a suffix with the date and the zip extension
		os.chdir(logsdir) 												# Change directory to the logsdir
		os.system(zip_program + " " +  files1 +" "+ files)	# Zip the logs into dated zip files for each server. - 1.1
		os.remove(files)													# Remove the original log files# Script Name		: create_dir_if_not_there.py
# Author				: Craig Richards
# Created				: 09th January 2012
# Last Modified		: 
# Version				: 1.0
# Modifications		: 

# Description			: Checks to see if a directory exists in the users home directory, if not then create it

import os												# Import the OS module
home=os.path.expanduser("~")				# Set the variable home by expanding the users set home directory
print home												# Print the location
if not os.path.exists(home+'/testdir'):		# Check to see if the directory exists
  os.makedirs(home+'/testdir')					# If not create the directory, inside their home directory# Script Name		: move_files_over_x_days.py# Author				: Craig Richards# Created				: 8th December 2011# Last Modified		: # Version				: 1.0# Modifications		: # Description			: This will move all the files from the src directory that are over 240 days old to the destination directory.import shutil, sys, time, os								# Import the header filessrc = 'u:\\test'												# Set the source directorydst = 'c:\\test'												# Set the destination directorynow = time.time()											# Get the current timefor f in os.listdir(src):										# Loop through all the files in the source directory    if os.stat(f).st_mtime < now - 240 * 86400:	# Work out how old they are, if they are older than 240 days old        if os.path.isfile(f):									# Check it's a file            shutil.move(f, dst)								# Move the files 			# Script Name		: puttylogs.py
# Author				: Craig Richards
# Created				: 13th October 2011
# Last Modified		: 29th February 2012
# Version				: 1.2

# Modifications		: 1.1 - Added the variable zip_program so you can set it for the zip program on whichever OS, so to run on a different OS just change the locations of these two variables.
#							: 1.2 - 29-02-12 - CR - Added shutil module and added one line to move the zipped up logs to the zipped_logs directory

# Description			: Zip up all the logs in the given directory

import os																	# Load the Library Module
import shutil																# Load the Library Module - 1.2
from time import strftime												# Load just the strftime Module from Time

logsdir="c:\logs\puttylogs"											# Set the Variable logsdir
zipdir="c:\logs\puttylogs\zipped_logs"							# Set the Variable zipdir - 1.2
zip_program="zip.exe"												# Set the Variable zip_program - 1.1

for files in os.listdir(logsdir):										# Find all the files in the directory
	if files.endswith(".log"):											# Check to ensure the files in the directory end in .log
		files1=files+"."+strftime("%Y-%m-%d")+".zip"		# Create the Variable files1, this is the files in the directory, then we add a suffix with the date and the zip extension
		os.chdir(logsdir) 												# Change directory to the logsdir
		os.system(zip_program + " " +  files1 +" "+ files)	# Zip the logs into dated zip files for each server. - 1.1
		shutil.move(files1, zipdir)									# Move the zipped log files to the zipped_logs directort - 1.2
		os.remove(files)													# Remove the original log files
		# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

import subprocess										# Import the subprocess module
for server in open('server_list.txt'):				# Open the file and read each line
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
			f.write (subnet+"."+str(ip) + " did not respond" + "\n")	# Write out you can't reach the box# Script Name		: ping_servers.py
# Author				: Craig Richards
# Created				: 9th May 2012
# Last Modified		: 14th May 2012
# Version				: 1.1

# Modifications		: 1.1 - 14th May 2012 - CR Changed it to use the config directory to store the server files

# Description			: This script will, depending on the arguments supplied will ping the servers associated with that application group.

import os							# Load the Library Module
import subprocess				# Load the Library Module 
import sys							# Load the Library Module

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:	# Help Menu if called
    print '''
You need to supply the application group for the servers you want to ping, i.e.
	dms
	swaps 
	
Followed by the site i.e.
	155
	bromley'''
    sys.exit(0)
else:

	if (len(sys.argv) < 3): 																# If no arguments are passed,display the help/instructions on how to run the script
		sys.exit ('\nYou need to supply the app group. Usage : ' + filename + ' followed by the application group i.e. \n \t dms or \n \t swaps \n then the site i.e. \n \t 155 or \n \t bromley')

	appgroup = sys.argv[1]															# Set the variable appgroup as the first argument you supply
	site = sys.argv[2]																	# Set the variable site as the second argument you supply
	
	if os.name == "posix":															# Check the os, if it's linux then			
		myping = "ping -c 2 "															# This is the ping command
	elif os.name in ("nt", "dos", "ce"):											# Check the os, if it's windows then
		myping = "ping -n 2 "															# This is the ping command
	
	if 'dms' in sys.argv:																	# If the argument passed is dms then
	  appgroup = 'dms'																	# Set the variable appgroup to dms
	elif 'swaps' in sys.argv:															# Else if the argment passed is swaps then
	  appgroup = 'swaps'																# Set the variable appgroup to swaps
	  
	if '155' in sys.argv:																	# If the argument passed is 155 then
	  site = '155'																			# Set the variable site to 155
	elif 'bromley' in sys.argv:															# Else if the argument passed is bromley
	  site = 'bromley'																	# Set the variable site to bromley

filename = sys.argv[0]																# Sets a variable for the script name
logdir = os.getenv("logs")															# Set the variable logdir by getting the OS environment logs
logfile = 'ping_'+appgroup+'_'+site+'.log'										# Set the variable logfile, using the arguments passed to create the logfile
logfilename=os.path.join(logdir, logfile)											# Set the variable logfilename by joining logdir and logfile together
confdir = os.getenv("my_config")													# Set the variable confdir from the OS environment variable - 1.2
conffile = (appgroup+'_servers_'+site+'.txt')									# Set the variable conffile - 1.2
conffilename=os.path.join(confdir, conffile)									# Set the variable conffilename by joining confdir and conffile together - 1.2

f = open(logfilename, "w")															# Open a logfile to write out the output
for server in open(conffilename):													# Open the config file and read each line - 1.2
	ret = subprocess.call(myping + server, shell=True,stdout=f,stderr=subprocess.STDOUT)	# Run the ping command for each server in the list.
	if ret == 0:																				# Depending on the response
	  f.write (server.strip() + " is alive" + "\n")									# Write out that you can receive a reponse
	else: 
	  f.write (server.strip() + " did not respond" + "\n")						# Write out you can't reach the box
	 
print ("\n\tYou can see the results in the logfile : "+ logfilename);	# Show the location of the logfile# Script Name		: fileinfo.py
# Author				: Not sure where I got this from
# Created				: 28th November 2011
# Last Modified		: 
# Version				: 1.0
# Modifications		: 

# Description			: Show file information for a given file


# get file information using os.stat()
# tested with Python24 vegsaeat 25sep2006
import os
import stat # index constants for os.stat()
import time
# pick a file you have ...
file_name = raw_input("Enter a file name: ")
file_stats = os.stat(file_name)
# create a dictionary to hold file info
file_info = {
  'fname': file_name,
  'fsize': file_stats [stat.ST_SIZE],
  'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
  'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_ATIME])),
  'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
}
print
print "file name = %(fname)s" % file_info
print "file size = %(fsize)s bytes" % file_info
print "last modified = %(f_lm)s" % file_info
print "last accessed = %(f_la)s" % file_info
print "creation time = %(f_ct)s" % file_info
print
if stat.S_ISDIR(file_stats[stat.ST_MODE]):
  print "This a directory"
else:
  print "This is not a directory"
  print
  print "A closer look at the os.stat(%s) tuple:" % file_name
  print file_stats
  print
  print "The above tuple has the following sequence:"
  print """st_mode (protection bits), st_ino (inode number),
  st_dev (device), st_nlink (number of hard links),
  st_uid (user ID of owner), st_gid (group ID of owner),
  st_size (file size, bytes), st_atime (last access time, seconds since epoch),
  st_mtime (last modification time), st_ctime (time of creation, Windows)"""# Script Name		: dir_test.py
# Author				: Craig Richards
# Created				: 29th November 2011
# Last Modified		:
# Version				: 1.0
# Modifications		: 

# Description			: Tests to see if the directory testdir exists, if not it will create the directory for you

import os									# Import the OS module
if not os.path.exists('testdir'):		#  Check to see if it exists  
  os.makedirs('testdir')				#  Create the directory # Script Name		: env_check.py
# Author				: Craig Richards
# Created				: 14th May 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This script will check to see if all of the environment variables I require are set

import os

confdir = os.getenv("my_config")												# Set the variable confdir from the OS environment variable
conffile = 'env_check.conf'														# Set the variable conffile
conffilename=os.path.join(confdir, conffile)								# Set the variable conffilename by joining confdir and conffile together

for env_check in open(conffilename):										# Open the config file and read all the settings
  env_check = env_check.strip()												# Set the variable as itsself, but strip the extra text out
  print '[{}]'.format(env_check)													# Format the Output to be in Square Brackets
  newenv = os.getenv(env_check)											# Set the variable newenv to get the settings from the OS what is currently set for the settings out the configfile
  if newenv is None:																# If it doesn't exist
    print env_check, 'is not set'													# Print it is not set
  else:																					# Else if it does exist
    print 'Current Setting for {}={}\n'.format(env_check, newenv)	# Print out the details# Script Name		: script_count.py
# Author				: Craig Richards
# Created				: 27th February 2012
# Last Modified		: 
# Version				: 1.1

# Modifications		: 1.1 - 28-02-2012 - CR - Changed inside github and development functions, so instead of if os.name = "posix" do this else do this etc 
#							: I used os.path.join, so it condensed 4 lines down to 1

# Description			: This simple script loads everything I need to carry out the daily checks for our systems.

import os																					# Load the library module

path = os.getenv("scripts") 															# Set the variable path by getting the value from the OS environment variable scripts
dropbox = os.getenv("dropbox")													# Set the variable dropbox by getting the value from the OS environment variable dropbox

def clear_screen():																		# Function to clear the screen
	if os.name == "posix":															# Unix/Linux/MacOS/BSD/etc
		os.system('clear')																# Clear the Screen
	elif os.name in ("nt", "dos", "ce"):											# DOS/Windows
		os.system('CLS')																# Clear the Screen

def count_files(path, extensions):     											# Start of the function to count the files in the scripts directory, it counts the extension when passed below
  counter = 0     																		# Set the counter to 0
  for root, dirs, files in os.walk(path):        									# Loop through all the directories in the given path 
    for file in files:             															# For all the files
	  counter += file.endswith(extensions)										# Count the files
  return counter  																		# Return the count

def github():   																			# Start of the function just to count the files in the github directory
  github_dir = os.path.join(dropbox, 'github')									# Joins the paths to get the github directory - 1.1
  github_count = sum((len(f) for _, _, f in os.walk(github_dir)))			# Get a count for all the files in the directory
  if github_count > 5:																	# If the number of files is greater then 5, then print the following messages
    print '\nYou have too many in here, start uploading !!!!!'
    print 'You have: ' + str(github_count) + ' waiting to be uploaded to github!!'
  elif github_count == 0:																# Unless the count is 0, then print the following messages
    print '\nGithub directory is all Clear'
  else:																						# If it is any other number then print the following message, showing the number outstanding.
	print '\nYou have: ' + str(github_count) + ' waiting to be uploaded to github!!'
  
def development():   																	# Start of the function just to count the files in the development directory
  dev_dir = os.path.join(path, 'development')									# Joins the paths to get the development directory - 1.1
  dev_count = sum((len(f) for _, _, f in os.walk(dev_dir)))					# Get a count for all the files in the directory
  if dev_count > 10:																	# If the number of files is greater then 10, then print the following messages
    print '\nYou have too many in here, finish them or delete them !!!!!'
    print 'You have: ' + str(dev_count) + ' waiting to be finished!!'
  elif dev_count ==0:																	# Unless the count is 0, then print the following messages
    print '\nDevelopment directory is all clear'
  else:
	print '\nYou have: ' + str(dev_count) + ' waiting to be finished!!'	# If it is any other number then print the following message, showing the number outstanding.

clear_screen()																			# Call the function to clear the screen
	
print '\nYou have the following :\n'  
print 'AutoIT:\t' + str(count_files(path, '.au3'))									# Run the count_files function to count the files with the extension we pass
print 'Perl:\t' + str(count_files(path, '.pl'))
print 'Python:\t' + str(count_files(path, '.py'))
print 'Shell:\t' + str(count_files(path, ('.ksh', '.sh', '.bash')))
print 'SQL:\t' + str(count_files(path, '.sql'))

github()																						# Call the github function
development()																			# Call the development function# Script Name		: script_listing.py
# Author				: Craig Richards
# Created				: 15th February 2012
# Last Modified		: 
# Version				: 1.1
# Modifications		: 1.1 - 28-02-2012 - CR - Added the variable to get the logs directory, I then joined the output so the file goes to the logs directory

# Description			: This will list all the files in the given directory, it will also go through all the subdirectories as well

import os																		# Load the library module							

logdir = os.getenv("logs")												# Set the variable logdir by getting the value from the OS environment variable logs
logfile = 'script_list.log'													# Set the variable logfile

path = (raw_input("Enter dir: "))										# Ask the user for the directory to scan
logfilename=os.path.join(logdir, logfile)								# Set the variable logfilename by joining logdir and logfile together
log = open(logfilename, 'w')												# Set the variable log and open the logfile for writing
for dirpath, dirname, filenames in os.walk(path):				# Go through the directories and the subdirectories
  for filename in filenames:												# Get all the filenames
	log.write(os.path.join(dirpath, filename)+'\n')					# Write the full path out to the logfile
print "\nYour logfile " , logfilename, "has been created"		# Small message informing the user the file has been created