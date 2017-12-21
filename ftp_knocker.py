## THINGS to do::::! -- must get sleep
## add a subnet validator == valid_ip method
## check performance of ipaddress module vs socket for host scanning a network
## naming conventions???? clean up code???? 
## in time clean up by adding more functionality to existing functions, using real exception handling

import socket
import sys
import subprocess
import platform
from ftplib import FTP 


def main():
	if platform.system() == 'Windows':
		subprocess.call('cls', shell=True)
	elif platform.system() == 'Linux':
		subprocess.call('clear', shell=True)
	else:
		None

	# get ip range from user ex.(192.168.1.1/24)
	usersTarget = input("What is the ip range you want to scan?\n(Example: 192.168.1.1/24)\n\n:/> ")
	ipAddress = usersTarget.split('/')

	if len(ipAddress) > 2:
		print("\nToo much info; What the hell did you type?\ntry something like 192.168.1.1/24 || a.k.a [IP address][backslash][subnet mask]")
	elif len(ipAddress) < 2:
		print("\nNot enough info; What the hell did you type?\ntry something like 192.168.1.1/24 || a.k.a [IP address][backslash][subnet mask]")
	else:	
		if valid_ip(ipAddress[0]) == True:
			print("\nSeems to be a valid IP... let's have crack at it, eh?!\n\n")
			print("-"*120)
			print("\tPlease hold onto your panties because we are doing a scannies... shutup i was drunk while coding this,**buuerrerrrp*")
			print("-"*120)

			networkScan(str(ipAddress))
		else:
			sys.exit()


def valid_ip(testADDR):
    try: 
        socket.inet_aton(testADDR)
        return True
    except:
   		print('\n{} is not a valid IP address.\n\n*\\.*\\.*\\.*\\.Exiting./*./*./*./*'.format(testADDR))
   		return False

def networkScan(ipRange):
	targetNet = ipaddress.ip_network(ipRange)
	for node in targetNet.hosts():
		hostScan(node)


def hostScan(host):	
	socket = socket.socket(AF_INET, SOCK_STREAM)



if __name__ == "__main__":
	main()