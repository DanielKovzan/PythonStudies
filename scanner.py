###########################################
# Credit to The Cyber Mentor on youtube
############################################
#!/bin/python3

import sys
import socket
from datetime import datetime 

#Define our target
if len(sys.argv) == 2:
	target =  socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
	print("Invalid amount of arguements.")
	print("Synthax. python3 scanner.py<ip>")
	
#add a banenr
print("-" * 50)
print("Scanning Target {}".format(target))
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator, if open, returns 0, if error/closed, returns 1
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname couldn not be resolved.")
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
