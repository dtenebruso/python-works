from sys import argv
from os.path import exists
import time

#unpacking and decalring variables with selected files
script, from_file, to_file = argv

print("Copying from %s to %s..." % (from_file,to_file))

#open the file and copy it's contents
in_file = open(from_file, 'r')
indata = in_file.read()

print("\n\nThe file is %d bytes long" % len(indata))

#check to see if output file exists and ask for confirmation to continue
print("Checking if output file exists...%r" % exists(to_file))
print("To continue, hit ENTER, to cancel CTRL-C")
input()

print("\n\n....")
out_file = open(to_file, 'w')
out_file.write(indata)
time.sleep(2)

print("\nCopy is complete")

out_file.close()
in_file.close()
