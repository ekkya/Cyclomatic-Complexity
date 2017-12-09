# Script Name		: pscheck.py
# Author				: Craig Richards
# Created				: 19th December 2011
# Last Modified		: 17th June 2013
# Version				: 1.1

# Modifications		: 1.1 - 17/06/13 - CR - Changed to functions, and check os before running the program

# Description			: Process check on Nix boxes, diplsay formatted output from ps command

import commands, os, string

def ps():
  program = raw_input("Enter the name of the program to check: ")

  try:
    #perform a ps command and assign results to a list
    output = commands.getoutput("ps -f|grep " + program)
    proginfo = string.split(output)

    #display results
    print "\n\
    Full path:\t\t", proginfo[5], "\n\
    Owner:\t\t\t", proginfo[0], "\n\
    Process ID:\t\t", proginfo[1], "\n\
    Parent process ID:\t", proginfo[2], "\n\
    Time started:\t\t", proginfo[4]
  except:
    print "There was a problem with the program." 

def main():
  if os.name == "posix":											# Unix/Linux/MacOS/BSD/etc
    ps()																	# Call the function
  elif os.name in ("nt", "dos", "ce"):							# if the OS is windows
    print "You need to be on Linux or Unix to run this"
		 
		 
if __name__ == '__main__':
  main()# Script Name	: new_script.py
# Author			: Craig Richards
# Created			: 20th November 2012
# Last Modified	: 
# Version			: 1.0

# Modifications	: 

# Description		: This will create a new basic template for a new script

import os				# Load the library module
import sys				# Load the library module
import datetime		# Load the library module

text = '''You need to pass an argument for the new script you want to create, followed by the script name.  You can use
	-python	: Python Script
	-bash	: Bash Script
	-ksh	: Korn Shell Script
	-sql	: SQL Script'''

if len(sys.argv) < 3:
  print text				
  sys.exit()			
  
if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:	
  print text																									
  sys.exit()																								
else:	
  if '-python' in sys.argv[1]:
    config_file="python.cfg"
    extension=".py"
  elif '-bash' in sys.argv[1]:
    config_file="bash.cfg"
    extension=".bash"
  elif '-ksh' in sys.argv[1]:
    config_file="ksh.cfg"
    extension=".ksh"
  elif '-sql' in sys.argv[1]:
    config_file="sql.cfg"
    extension=".sql"
  else:
    print 'Unknown option - ' + text						
    sys.exit()

confdir=os.getenv("my_config")
scripts=os.getenv("scripts")
dev_dir="Development"
newfile=sys.argv[2]
output_file=(newfile+extension)
outputdir=os.path.join(scripts,dev_dir)
script=os.path.join(outputdir, output_file)
input_file=os.path.join(confdir,config_file)
old_text=" Script Name	: "
new_text=(" Script Name	: "+output_file)
newscript = open(script, 'w')								
input=open(input_file,'r')
today=datetime.date.today()
old_date= " Created	:"
new_date= (" Created	: "+today.strftime("%d %B %Y"))
	
for line in input:			
  line = line.replace(old_text, new_text)
  line = line.replace(old_date, new_date)
  newscript.write(line)				# Script Name		: osinfo.py
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
platform.release(),
platform.system(),
platform.uname(),
platform.version(),
]
i=1
for item in profile:
  print '#',i,' ',item
  i=i+1;# Script Name		: logs.py
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
		os.remove(files)													# Remove the original log files# Script Name	: check_for_sqlite_files.py
# Author		: Craig Richards
# Created		: 07 June 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Scans directories to check if there are any sqlite files in there 

import os

def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return False
    else:
        fd = open(filename, 'rb')
        Header = fd.read(100)
        fd.close()

        if Header[0:16] == 'SQLite format 3\000':
            return True
        else:
            return False

log=open('sqlite_audit.txt','w')
for r,d,f in os.walk(r'.'):
  for files in f:
    if isSQLite3(files):
	  print files
	  print "[+] '%s' **** is a SQLITE database file **** " % os.path.join(r,files)
	  log.write("[+] '%s' **** is a SQLITE database file **** " % files+'\n')
    else:
	  log.write("[-] '%s' is NOT a sqlite database file" % os.path.join(r,files)+'\n')
	  log.write("[-] '%s' is NOT a sqlite database file" % files+'\n')# Script Name		: create_dir_if_not_there.py
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
  os.makedirs(home+'/testdir')					# If not create the directory, inside their home directory# Script Name		: move_files_over_x_days.py# Author				: Craig Richards# Created				: 8th December 2011# Last Modified		: # Version				: 1.0# Modifications		: # Description			: This will move all the files from the src directory that are over 240 days old to the destination directory.import shutil, sys, time, os								# Import the header filessrc = 'u:\\test'												# Set the source directorydst = 'c:\\test'												# Set the destination directorynow = time.time()											# Get the current timefor f in os.listdir(src):										# Loop through all the files in the source directory    if os.stat(f).st_mtime < now - 240 * 86400:	# Work out how old they are, if they are older than 240 days old        if os.path.isfile(f):									# Check it's a file            shutil.move(f, dst)								# Move the files 			# Script Name	: sqlite_table_check.py
# Author		: Craig Richards
# Created		: 07 June 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Checks the main SQLITE database to ensure all the tables should exist


import sqlite3 
import sys
import os

dropbox= os.getenv("dropbox")
config=os.getenv("my_config")
dbfile=("Databases\jarvis.db")
listfile=("sqlite_master_table.lst")
master_db=os.path.join(dropbox, dbfile)
config_file=os.path.join(config, listfile)
tablelist=open(config_file,'r');

conn = sqlite3.connect(master_db)
cursor = conn.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
data = cursor.fetchone()

if str(data) == "(u'3.6.21',)":
  print ("\nCurrently " + master_db + " is on SQLite version: %s" % data + " - OK -\n")
else:
  print ("\nDB On different version than master version - !!!!! \n")
conn.close()

print ("\nCheckling " + master_db + " against " + config_file + "\n")

for table in tablelist.readlines():
  conn = sqlite3.connect(master_db)
  cursor = conn.cursor()
  cursor.execute("select count(*) from sqlite_master where name = ?",(table.strip(), ))
  res = cursor.fetchone()
    
  if (res[0]):
    print ('[+] Table : ' + table.strip() + ' exists [+]')
  else:
    print ('[-] Table : ' + table.strip() + '  does not exist [-]')
  # Script Name		: puttylogs.py
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
		shutil.move(files1, zipdir)									# Move the zipped log files to the zipped_logs directory - 1.2
		os.remove(files)													# Remove the original log files
		# Script Name		: daily_checks.py
# Author				: Craig Richards
# Created				: 07th December 2011
# Last Modified		: 01st May 2013
# Version				: 1.4

# Modifications		: 1.1 Removed the static lines for the putty sessions, it now reads a file, loops through and makes the connections.
#							: 1.2 Added a variable filename=sys.argv[0] , as when you use __file__ it errors when creating an exe with py2exe.
#							: 1.3 Changed the server_list.txt file name and moved the file to the config directory.
#							: 1.4 Changed some settings due to getting a new pc

# Description			: This simple script loads everything I need to carry out the daily checks for our systems.

import platform					# Load the Library Module
import os							# Load the Library Module
import subprocess				# Load the Library Module 
import sys							# Load the Library Module

from time import strftime		# Load just the strftime Module from Time

def clear_screen():								# Function to clear the screen
	if os.name == "posix":					# Unix/Linux/MacOS/BSD/etc
		os.system('clear')						# Clear the Screen
	elif os.name in ("nt", "dos", "ce"):	# DOS/Windows
		os.system('CLS')						# Clear the Screen

def print_docs():									# Function to print the daily checks automatically
  print "Printing Daily Check Sheets:"
  # The command below passes the command line string to open word, open the document, print it then close word down
  subprocess.Popen(["C:\\Program Files (x86)\Microsoft Office\Office14\winword.exe", "P:\\\\Documentation\\Daily Docs\\Back office Daily Checks.doc", "/mFilePrintDefault", "/mFileExit"]).communicate() 
  
def putty_sessions():										# Function to load the putty sessions I need
  for server in open(conffilename):					# Open the file server_list.txt, loop through reading each line - 1.1 -Changed - 1.3 Changed name to use variable conffilename
    subprocess.Popen(('putty -load '+server))		# Open the PuTTY sessions - 1.1
	  
def rdp_sessions():
  print "Loading RDP Sessions:"
  subprocess.Popen("mstsc eclr.rdp")				# Open up a terminal session connection and load the euroclear session
  
def euroclear_docs():
  # The command below opens IE and loads the Euroclear password document
  subprocess.Popen('"C:\\Program Files\\Internet Explorer\\iexplore.exe"' '"file://fs1\pub_b\Pub_Admin\Documentation\Settlements_Files\PWD\Eclr.doc"')

# End of the functions			

# Start of the Main Program

filename=sys.argv[0]									# Create the variable filename
confdir = os.getenv("my_config")					# Set the variable confdir from the OS environment variable - 1.3
conffile = ('daily_checks_servers.conf')			# Set the variable conffile - 1.3
conffilename=os.path.join(confdir, conffile)	# Set the variable conffilename by joining confdir and conffile together - 1.3
clear_screen()											# Call the clear screen function
# The command below prints a little welcome message, as well as the script name, the date and time and where it was run from.
print "Good Morning " + os.getenv('USERNAME') + ", " + filename, "ran at", strftime("%Y-%m-%d %H:%M:%S"), "on",platform.node(), "run from",os.getcwd()
print_docs()												# Call the print_docs function
putty_sessions()										# Call the putty_session function
rdp_sessions()											# Call the rdp_sessions function
euroclear_docs()										# Call the euroclear_docs function# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

import subprocess										# Import the subprocess module
for server in open('server_list.txt'):				# Open the file and read each line
	subprocess.Popen(('nslookup '+server))	# Run the nslookup command for each server in the list# Script Name	: portscanner.py
# Author		: Craig Richards
# Created		: 20 May 2013 
# Last Modified	: 
# Version		: 1.0

# Modifications	: 

# Description	: Port Scanner, you just pass the host and the ports

import optparse				# Import the module
from socket import *		# Import the module
from threading import *		# Import the module

screenLock = Semaphore(value=1)		# Prevent other threads from preceeding

def connScan(tgtHost, tgtPort):		# Start of the function
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)	# Open a socket
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('')
		results=connSkt.recv(100)
		screenLock.acquire()		# Acquire the lock
		print '[+] %d/tcp open'% tgtPort
		print '[+] ' + str(results)
	except:
		screenLock.acquire()
		print '[-] %d/tcp closed '% tgtPort
	finally:
		screenLock.release()
		connSkt.close()
		
def portScan(tgtHost, tgtPorts):	# Start of the function
	try:
		tgtIP = gethostbyname(tgtHost)	# Get the IP from the hostname
	except:
		print "[-] Cannot resolve '%s': Unknown host"%tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)	# Get hostname from IP
		print '\n[+] Scan Results for: ' +tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:	# Scan host and ports
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('usage %prog -H'+' <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort',type='string', help='specify target port[s] seperated by a comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
	main()# Script Name		: work_connect.py
# Author				: Craig Richards
# Created				: 11th May 2012
# Last Modified		: 31st October 2012
# Version				: 1.1

# Modifications		: 1.1 - CR - Added some extra code, to check an argument is passed to the script first of all, then check it's a valid input

# Description			: This simple script loads everything I need to connect to work etc

import subprocess				# Load the Library Module 
import sys							# Load the Library Module 
import os							# Load the Library Module
import time						# Load the Library Module

dropbox = os.getenv("dropbox")							# Set the variable dropbox, by getting the values of the environment setting for dropbox
rdpfile = ("remote\\workpc.rdp")							# Set the variable logfile, using the arguments passed to create the logfile
conffilename=os.path.join(dropbox, rdpfile)			# Set the variable conffilename by joining confdir and conffile together
remote = (r"c:\windows\system32\mstsc.exe ")	# Set the variable remote with the path to mstsc

text = '''You need to pass an argument
	-c Followed by login password to connect
	-d to disconnect'''											# Text to display if there is no argument passed or it's an invalid option - 1.2

if len(sys.argv) < 2:											# Check there is at least one option passed to the script - 1.2
  print text															# If not print the text above - 1.2
  sys.exit()														# Exit the program - 1.2
  
if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:	# Help Menu if called
    print text														# Print the text, stored in the text variable - 1.2
    sys.exit(0)														# Exit the program
else:
  if sys.argv[1].lower().startswith('-c'):					# If the first argument is -c then
    passwd = sys.argv[2] 									# Set the variable passwd as the second argument passed, in this case my login password
    subprocess.Popen((r"c:\Program Files\Checkpoint\Endpoint Connect\trac.exe connect -u username -p "+passwd))
    subprocess.Popen((r"c:\geektools\puttycm.exe"))
    time.sleep(15)												# Sleep for 15 seconds, so the checkpoint software can connect before opening mstsc
    subprocess.Popen([remote, conffilename])
  elif sys.argv[1].lower().startswith('-d'):					# If the first argument is -d then disconnect my checkpoint session.
    subprocess.Popen((r"c:\Program Files\Checkpoint\Endpoint Connect\trac.exe disconnect "))
  else:
    print 'Unknown option - ' + text						# If any other option is passed, then print Unknown option and the text from above - 1.2# Script Name		: testlines.py
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
f.close()									# Close the file
# Script Name		: ping_subnet.py
# Author				: Craig Richards
# Created				: 12th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: After supplying the first 3 octets it will scan the final range for available addresses

import os						# Load the Library Module
import subprocess			# Load the Library Module 
import sys						# Load the Library Module

filename = sys.argv[0]																				# Sets a variable for the script name

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:	# Help Menu if called
    print '''
You need to supply the first octets of the address Usage : ''' + filename + ''' 111.111.111 '''
    sys.exit(0)
else:

	if (len(sys.argv) < 2): 																				# If no arguments are passed then display the help and instructions on how to run the script
		sys.exit (' You need to supply the first octets of the address Usage : ' + filename + ' 111.111.111')

	subnet = sys.argv[1]																				# Set the variable subnet as the three octets you pass it
	
	if os.name == "posix":																			# Check the os, if it's linux then			
		myping = "ping -c 2 "																			# This is the ping command
	elif os.name in ("nt", "dos", "ce"):															# Check the os, if it's windows then
		myping = "ping -n 2 "																			# This is the ping command

	f = open('ping_'+subnet+'.log', 'w')															# Open a logfile
	for ip in range(2,255):																				# Set the ip variable for the range of numbers
		ret = subprocess.call(myping + str(subnet)+"."+str(ip) , shell=True,stdout=f,stderr=subprocess.STDOUT) # Run the command pinging the servers
		if ret == 0:																							# Depending on the response
			f.write (subnet+"."+str(ip) + " is alive" + "\n")									# Write out that you can receive a reponse
		else: 
			f.write (subnet+"."+str(ip) + " did not respond" + "\n")						# Write out you can't reach the box# Script Name		: ping_servers.py
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
	 
print ("\n\tYou can see the results in the logfile : "+ logfilename);	# Show the location of the logfile# Script Name	: backup_automater_services.py
# Author			: Craig Richards
# Created			: 24th October 2012
# Last Modified	:
# Version			: 1.0

# Modifications	: 

# Description		: This will go through and backup all my automator services workflows

import shutil							# Load the library module
import datetime						# Load the library module
import os								# Load the library module

today=datetime.date.today()	# Get Today's date
todaystr=today.isoformat()		# Format it so we can use the format to create the directory

confdir=os.getenv("my_config")					# Set the variable by getting the value from the OS setting
dropbox=os.getenv("dropbox") 					# Set the variable by getting the value from the OS setting
conffile = ('services.conf') 							# Set the variable as the name of the configuration file
conffilename=os.path.join(confdir, conffile)  	# Set the variable by combining the path and the file name
sourcedir=os.path.expanduser('~/Library/Services/')													# Source directory of where the scripts are located
destdir=os.path.join(dropbox, "My_backups"+"/"+"Automater_services"+todaystr+"/") # Combine several settings to create the destination backup directory

for file_name in open(conffilename): 									# Walk through the configuration file
  fname = file_name.strip()													# Strip out the blank lines from the configuration file
  if fname:																			# For the lines that are not blank
    sourcefile=os.path.join(sourcedir, file_name.strip())			# Get the name of the source files to backup
    destfile=os.path.join(destdir, file_name.strip()) 					# Get the name of the destination file names
    shutil.copytree(sourcefile, destfile)									# Copy the directories# Script Name		: powerup_checks.py
# Author				: Craig Richards
# Created				: 25th June 2013
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: Creates an output file by pulling all the servers for the given site from SQLITE database, then goes through the list pinging the servers to see if they are up on the network

import sys							# Load the Library Module 
import sqlite3					# Load the Library Module 	
import os							# Load the Library Module 
import subprocess				# Load the Library Module 
from time import strftime		# Load just the strftime Module from Time


dropbox=os.getenv("dropbox")															# Set the variable, by getting the value of the variable from the OS
config=os.getenv("my_config")														# Set the variable, by getting the value of the variable from the OS
dbfile=("Databases/jarvis.db")															# Set the variable to the database
master_db=os.path.join(dropbox, dbfile)											# Create the variable by linking the path and the file
listfile=("startup_list.txt")																# File that will hold the servers
serverfile=os.path.join(config,listfile)													# Create the variable by linking the path and the file
outputfile=('server_startup_'+strftime("%Y-%m-%d-%H-%M")+'.log')

# Below is the help text

text = '''

You need to pass an argument, the options the script expects is 

	-site1		For the Servers relating to site1
	-site2	For the Servers located in site2'''
	
def windows():																																			# This is the function to run if it detects the OS is windows.
	f = open(outputfile, 'a')																															# Open the logfile
	for server in open(serverfile,'r'):																													# Read the list of servers from the list
		#ret = subprocess.call("ping -n 3 %s" % server.strip(), shell=True,stdout=open('NUL', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
		ret = subprocess.call("ping -n 3 %s" % server.strip(),stdout=open('NUL', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
		if ret == 0:             																															# Depending on the response
		  f.write ("%s: is alive" % server.strip().ljust(15) + "\n")																			# Write out to the logfile is the server is up
		else: 
		  f.write ("%s: did not respond" % server.strip().ljust(15) + "\n")																# Write to the logfile if the server is down

			
def linux():																																					# This is the function to run if it detects the OS is nix.
	f = open('server_startup_'+strftime("%Y-%m-%d")+'.log', 'a')																		# Open the logfile
	for server in open(serverfile,'r'):																													# Read the list of servers from the list
		ret = subprocess.call("ping -c 3 %s" % server, shell=True,stdout=open('/dev/null', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
		if ret == 0:																																			# Depending on the response
			f.write ("%s: is alive" % server.strip().ljust(15) + "\n")																			# Write out to the logfile is the server is up
		else:             
			f.write ("%s: did not respond" % server.strip().ljust(15) + "\n")															# Write to the logfile if the server is down

def get_servers(query):																																# Function to get the servers from the database
  conn = sqlite3.connect(master_db)																											# Connect to the database
  cursor = conn.cursor()																																# Create the cursor
  cursor.execute('select hostname from tp_servers where location =?',(query,))												# SQL Statement
  print ('\nDisplaying Servers for : ' + query + '\n')
  while True:																																				# While there are results
    row = cursor.fetchone()																															# Return the results
    if row == None:
      break
    f = open(serverfile, 'a')																																# Open the serverfile
    f.write("%s\n" % str(row[0]))																													# Write the server out to the file
    print row[0]																																			# Display the server to the screen
    f.close()																																				# Close the file

def main():																																					# Main Function
  if os.path.exists(serverfile):																														# Checks to see if there is an existing server file
    os.remove(serverfile)																																# If so remove it
	
  if len(sys.argv) < 2:																																	# Check there is an argument being passed
    print text																																				# Display the help text if there isn't one passed
    sys.exit()																																				# Exit the script

  if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:													# If the ask for help
    print text																																				# Display the help text if there isn't one passed
    sys.exit(0)																																				# Exit the script after displaying help
  else:
    if sys.argv[1].lower().startswith('-site1'):																										# If the argument is site1
      query = 'site1'																																		# Set the variable to have the value site
    elif sys.argv[1].lower().startswith('-site2'):																								# Else if the variable is bromley
	  query = 'site2'																																	# Set the variable to have the value bromley	
    else:
      print '\n[-] Unknown option [-] ' + text																										# If an unknown option is passed, let the user know
      sys.exit(0)
  get_servers(query)																																	# Call the get servers funtion, with the value from the argument
  
  if os.name == "posix":																																# If the OS is linux.
	linux()																																					# Call the linux function
  elif os.name in ("nt", "dos", "ce"):																												# If the OS is Windows...
	windows()																																				# Call the windows function

  print ('\n[+] Check the log file ' + outputfile + ' [+]\n')																					# Display the name of the log
  
if __name__ == '__main__':
  main()																																						# Call the main function# Script Name	: password_cracker.py
# Author		: Craig Richards
# Created		: 20 May 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Old school password cracker using python

import crypt	# Import the module

def testPass(cryptPass):	# Start the function
  salt = cryptPass[0:2]
  dictFile=open('dictionary.txt','r')	# Open the dictionary file
  for word in dictFile.readlines():	# Scan through the file
    word=word.strip('\n')
    cryptWord=crypt.crypt(word,salt)	# Check for password in the file
    if (cryptWord == cryptPass):
      print "[+] Found Password: "+word+"\n"
      return
  print "[-] Password Not Found.\n"
  return

def main():
  passFile = open('passwords.txt')		# Open the password file
  for line in passFile.readlines():	# Read through the file
    if ":" in line:
      user=line.split(':')[0]
      cryptPass = line.split(':')[1].strip(' ') # Prepare the user name etc
      print "[*] Cracking Password For: "+user 
      testPass(cryptPass)				# Call it to crack the users password

if __name__ == "__main__":
  main()# Script Name	: check_file.py
# Author		: Craig Richards
# Created		: 20 May 2013 
# Last Modified	: 
# Version		: 1.0

# Modifications	: 

# Description	: Check a file exists and that we can read the file

import sys		# Import the Modules
import os		# Import the Modules

# Readfile Functions which open the file that is passed to the script

def readfile(filename):
	f = open(filename, 'r')
	line = f.read()
	print line

def main():
  if len(sys.argv) == 2:		# Check the arguments passed to the script
    filename = sys.argv[1]		# The filename is the first argument
    if not os.path.isfile(filename):	# Check the File exists
      print '[-] ' + filename + ' does not exist.'
      exit(0)
    if not os.access(filename, os.R_OK):	# Check you can read the file
      print '[-] ' + filename + ' access denied'
      exit(0)
  else:
    print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>' # Print usage if not all parameters passed/Checked
    exit(0)
  print '[+] Reading from : ' + filename	# Display Message and read the file contents
  readfile(filename)
  
if __name__ == '__main__':
  main()# Script Name		: nmap_scan.py
# Author				: Craig Richards
# Created				: 24th May 2013
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This scans my scripts directory and gives a count of the different types of scripts, you need nmap installed to run this

import nmap			# Import the module
import optparse		# Import the module

def nmapScan(tgtHost, tgtPort):									# Create the function, this fucntion does the scanning
  nmScan = nmap.PortScanner()
  nmScan.scan(tgtHost, tgtPort)
  state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
  print "[*] " + tgtHost + " tcp/"+tgtPort +" "+state
  
def main():																								# Main Program
  parser = optparse.OptionParser('usage%prog ' + '-H <host> -p <port>')		# Display options/help if required
  parser.add_option('-H', dest='tgtHost', type='string', help='specify host')
  parser.add_option('-p', dest='tgtPort', type='string', help='port')
  (options, args) = parser.parse_args()
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort).split(',')
  
  if (tgtHost == None) | (tgtPorts[0] == None):  
    print parser.usage
    exit(0)

  for tgtPort in tgtPorts:																			# Scan the hosts with the ports etc
    nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
  main()# Script Name	: sqlite_check.py
# Author		: Craig Richards
# Created		: 20 May 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Runs checks to check my SQLITE database


import sqlite3 as lite
import sys
import os

dropbox= os.getenv("dropbox")
dbfile=("Databases\jarvis.db")
master_db=os.path.join(dropbox, dbfile)
con = None

try:
    con = lite.connect(master_db)
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data


except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()


con = lite.connect(master_db)
cur=con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cur.fetchall()
for row in rows:
  print row

con = lite.connect(master_db)
cur=con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
while True:
  row = cur.fetchone()
  if row == None:
    break
  print row[0]# Script Name		: fileinfo.py
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
  os.makedirs('testdir')				#  Create the directory # Script Name		: batch_file_rename.py
# Author				: Craig Richards
# Created				: 6th August 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This will batch rename a group of files in a given directory, once you pass the current and new extensions

import os															# Load the library module
import sys															# Load the library module

work_dir=sys.argv[1]											# Set the variable work_dir with the first argument passed
old_ext=sys.argv[2]											# Set the variable work_dir with the first argument passed
new_ext=sys.argv[3]											# Set the variable work_dir with the first argument passed

files = os.listdir(work_dir)									# Set the variable files, by listing everything in the directory 
for filename in files:											# Loop through the files
  file_ext = os.path.splitext(filename)[1]				# Get the file extension
  if old_ext == file_ext:										# Start of the logic to check the file extensions, if old_ext = file_ext
    newfile = filename.replace(old_ext, new_ext)	# Set newfile to be the filename, replaced with the new extension
    os.rename(													# Write the files
	    os.path.join(work_dir, filename),
		os.path.join(work_dir, newfile))# Script Name		: recyclebin.py
# Author				: Craig Richards
# Created				: 07th June 2013
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: Scans the recyclebin and displays the files in there, originally got this script from the Violent Python book

import os					# Load the Module
import optparse			# Load the Module
from _winreg import *	# Load the Module

def sid2user(sid):		# Start of the function to gather the user
  try:
    key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
    (value, type) = QueryValueEx(key, 'ProfileImagePath')
    user = value.split('\\')[-1]
    return user
  except:
    return sid
	

def returnDir():			# Start of the function to search through the recyclebin
  dirs=['c:\\Recycler\\','C:\\Recycled\\','C:\\$RECYCLE.BIN\\']
  #dirs=['c:\\$RECYCLE.BIN\\']
  for recycleDir in dirs:
    if os.path.isdir(recycleDir):
	  return recycleDir
  return None
  
def findRecycled(recycleDir):	# Start of the function, list the contents of the recyclebin
  dirList = os.listdir(recycleDir)
  for sid in dirList:
    files = os.listdir(recycleDir + sid)
    user = sid2user(sid)
    print '\n[*] Listing Files for User: ' + str(user)
    for file in files:
	  print '[+] Found File: ' + str(file)
	  
def main():
  recycleDir = returnDir()
  findRecycled(recycleDir)
  
if __name__ == '__main__':
  main()# Script Name		: powerdown_startup.py
# Author				: Craig Richards
# Created				: 05th January 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This goes through the server list and pings the machine, if it's up it will load the putty session, if its not it will notify you.

import os							# Load the Library Module
import subprocess				# Load the Library Module 
from time import strftime		# Load just the strftime Module from Time

def windows():																							# This is the function to run if it detects the OS is windows.
	f = open('server_startup_'+strftime("%Y-%m-%d")+'.log', 'a')						# Open the logfile
	for server in open('startup_list.txt','r'):														# Read the list of servers from the list
		ret = subprocess.call("ping -n 3 %s" % server, shell=True,stdout=open('NUL', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
		if ret == 0:             																			# If you get a response.
			f.write ("%s: is alive, loading PuTTY session" % server.strip() + "\n")	# Write out to the logfile
			subprocess.Popen(('putty -load '+server))											# Load the putty session
		else: 
			f.write ("%s : did not respond" % server.strip() + "\n")						# Write to the logfile if the server is down

def linux():
	f = open('server_startup_'+strftime("%Y-%m-%d")+'.log', 'a')						# Open the logfile
	for server in open('startup_list.txt'):															# Read the list of servers from the list
		ret = subprocess.call("ping -c 3 %s" % server, shell=True,stdout=open('/dev/null', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
		if ret == 0:																							# If you get a response.
			f.write ("%s: is alive" % server.strip() + "\n")										# Print a message
			subprocess.Popen(['ssh', server.strip()])
		else:             
			f.write ("%s: did not respond" % server.strip() + "\n")

# End of the functions			

# Start of the Main Program

if os.name == "posix":					# If the OS is linux...
	linux()										# Call the linux function
elif os.name in ("nt", "dos", "ce"):	# If the OS is Windows...
	windows()									# Call the windows function# Script Name		: folder_size.py
# Author				: Craig Richards
# Created				: 19th July 2012
# Last Modified		: 
# Version				: 1.0

# Modifications		: 

# Description			: This will scan the current directory and all subdirectories and display the size.

import os 														# Load the library module

directory = '.'													# Set the variable directory to be the current directory
dir_size = 0													# Set the size to 0
for (path, dirs, files) in os.walk(directory):			# Walk through all the directories
  for file in files:												# Get all the files
    filename = os.path.join(path, file)
    dir_size += os.path.getsize(filename)			# Get the sizes, the following lines print the sizes in bytes, Kb, Mb and Gb
print "Folder Size in Bytes = %0.2f Bytes" % (dir_size)
print "Folder Size in Kilobytes = %0.2f KB" % (dir_size/1024.0)
print "Folder Size in Megabytes = %0.2f MB" % (dir_size/1024/1024.0)
print "Folder Size in Gigabytes = %0.2f GB" % (dir_size/1024/1024/1024.0)# Script Name		: env_check.py
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
# Last Modified		: 20th July 2012
# Version				: 1.3

# Modifications		: 1.1 - 28-02-2012 - CR - Changed inside github and development functions, so instead of if os.name = "posix" do this else do this etc 
#							: I used os.path.join, so it condensed 4 lines down to 1
#							: 1.2 - 10-05-2012 - CR - Added a line to include PHP scripts.
#							: 1.3 - 20-07-2012 - CR - Added the line to include Batch scripts

# Description			: This scans my scripts directory and gives a count of the different types of scripts

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
print 'Batch:\t' + str(count_files(path, ('.bat', ',cmd')))						# 1.3
print 'Perl:\t' + str(count_files(path, '.pl'))
print 'PHP:\t' + str(count_files(path, '.php'))									# 1.2
print 'Python:\t' + str(count_files(path, '.py'))
print 'Shell:\t' + str(count_files(path, ('.ksh', '.sh', '.bash')))
print 'SQL:\t' + str(count_files(path, '.sql'))

github()																						# Call the github function
development()																			# Call the development function# Script Name		: script_listing.py
# Author				: Craig Richards
# Created				: 15th February 2012
# Last Modified		: 29th May 2012
# Version				: 1.2

# Modifications		: 1.1 - 28-02-2012 - CR - Added the variable to get the logs directory, I then joined the output so the file goes to the logs directory
#							: 1.2 - 29-05/2012 - CR - Changed the line so it doesn't ask for a directory, it now uses the environment varaible scripts

# Description			: This will list all the files in the given directory, it will also go through all the subdirectories as well

import os																		# Load the library module							

logdir = os.getenv("logs")												# Set the variable logdir by getting the value from the OS environment variable logs
logfile = 'script_list.log'													# Set the variable logfile
path = os.getenv("scripts")												# Set the varable path by getting the value from the OS environment variable scripts - 1.2

#path = (raw_input("Enter dir: "))										# Ask the user for the directory to scan
logfilename=os.path.join(logdir, logfile)								# Set the variable logfilename by joining logdir and logfile together
log = open(logfilename, 'w')												# Set the variable log and open the logfile for writing
for dirpath, dirname, filenames in os.walk(path):				# Go through the directories and the subdirectories
  for filename in filenames:												# Get all the filenames
	log.write(os.path.join(dirpath, filename)+'\n')					# Write the full path out to the logfile
print "\nYour logfile " , logfilename, "has been created"		# Small message informing the user the file has been created