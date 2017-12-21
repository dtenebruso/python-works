import socket
from ftplib import FTP 


def main():
	# get ip range from user ex.(192.168.1.1/24)
	usersTarget = input("What is the ip range you want to scan?\n(Example: 192.168.1.1/24)\n\n:/> ")
	ipAddress = usersTarget.split('/')

	if valid_ip(ipAddress[0]) == True:
		print("\nSeems to be a valid IP... let's have crack at it, eh?!\n\n")
		print("-"*120)
		print("Please hold onto your panties because we are doing a scannies... shutup i was drunk while coding this, imp")
		print("-"*120)

		targetScanner()
	else:
		None


def valid_ip(testADDR):
    try: 
        socket.inet_aton(testADDR)
        return True
    except:
   		print('{} is not a valid IP address'.format(testADDR))
   		return False


def targetScanner(address, range):	
	socket = socket.socket(AF_INET, SOCK_STREAM)



if __name__ == "__main__":
	main()