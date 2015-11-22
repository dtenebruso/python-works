from sys import argv
import time

script, filename = argv

print("We're going to erase %r." % filename)
print("If you do not want this, please hit CTRL-c now.")
print("If you wish to continue the hit ENTER...")

input('?')

print("\nOpening the file...")
target = open(filename, 'w')
time.sleep(2)

print("\n\nFile open. If you wish to proceed in truncating file %r hit ENTER, otherwise hit CTR-c" % filename)
input('?\n\n')

print("Truncating the file. Goodbye, %r!" % filename)
target.truncate()

print("\n\nLets put some new data in %r. Enter your name, age, address" % filename)

line1 = input("line 1: :")
line2 = input("line 2: :")
line3 = input("line 3: :")

print("\nWriting to file...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
time.sleep(1)

print("\nWriting is complete. Closing %r..." % filename)
target.close()
