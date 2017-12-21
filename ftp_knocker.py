import Sockets
from ftplib import FTP 



def main():
	# get ip range from user ex.(192.168.1.1/24)
	usersTarget = ("""What is the ip range you want to scan?\n
					(Example: 192.168.1.1/24)\n\n
					:/> """)
	ipAddress = "/".split(usersTarget)[0]
	valid_ip(ipAddress)

def valid_ip(testADDR):
    try: 
        socket.inet_aton(testADDR)
        return True
    except:
    	print("{}.format is not a valid IP address", testADDR)
        return False

def targetScanner(address, range)	
	socket = socket.socket(AF_INET, SOCK_STREAM)

