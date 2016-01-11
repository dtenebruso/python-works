import sys
import time
import random

security = 0
x = 0

while x != 1:
	print("Would you like to change your password, yes or no?\n")
	questionAns = input()
	if questionAns == "no":
		print("Okay enjoy the site\n\n")
		x = 1
	elif questionAns == "yes":
		print("Please enter your original password below\n")
		x = 1

print("Type your old password:")
oldPwd = input("")

time.sleep(3)

print("Thanks!\n\n")


while security != 1:
	print("Type your new password:\n\n")
	newPwd = input("")
	if newPwd == oldPwd:
		print("Your new password can not be the same as your latest password\n\n")
		security = 0

	elif newPwd != oldPwd:
		security = 1

clearance = 0

while clearance != 1:
	print("Type new password again for confirmation:")
	confirmPwd = input("")
	if confirmPwd != newPwd:
		print("Sorry try again...\n\n")
		clearance = 0
	elif confirmPwd == newPwd:
		print("Thanks!!!\n\n")
		clearance = 1

print("You can now Login using your new password")
