from sys import argv
from os.path import exists
import time

'''
Fake Situation:

your filesystem has been compromised by your best friends enemy. He is looking for the super secret file that contains the recipe to your space cake.
He knows the file location and the file name. Your mission is to copy the data in the target file create a new file in a different location with the copied data.
Then truncate the old file and finally write a virus that will execute upon him opening the file. Infecting his computer. All within one single program.

'''

script, origin_doc = argv

print("Opening %s..." % origin_doc)

file_open = open(origin_doc, 'r+')

file_data = file_open.read()

print("\n\nData has been copied")

print("\nName the new file: ")
new_filename = input()

new_filepath = "C:\\Users\\Guest\\Documents\\" + new_filename + ".bat"

print("Checking file existence...%r"% exists(new_filepath))
print("\nCreating and writing to file...")
new_fileopen = open(new_filepath, 'w')
new_fileopen.write(file_data)

print("\n\nWriting complete")
print("Closing %s" % new_filename)
new_fileopen.close()

file_open.close()

file_open = open(origin_doc, 'w+')

print("To proceed truncating %s, click ENTER, to abort hit CTRL-C" % origin_doc)
input()

file_open.truncate()

print("\nFile contents erased")

ans = input("Would you like to continue: y/n?")
if ans == 'y':
	print("To write virus type in the code and hit enter after each line. To finish. Type 'done'")
temp = 'n/a'
while temp != 'done':
	temp = input("VIRUS/code$# :")
	file_open.write(temp)
	file_open.write("\n")
print("writing virus to file...")
time.sleep(3)
print("Writing complete. Closing %s and exiting. Thank You!"% origin_doc)
file_open.close()
	
		



