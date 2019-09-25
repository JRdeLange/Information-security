import sys
import hashlib

# This function will read and save all of the lines entered
# after being called until EOF has been reached. It then 
# returns this as one long string.
def readInput():
	message = ''

	while True:
		line = sys.stdin.read()
		if line == '':
			break
		message += line

	return message

#This function return the SHA256 hash of its input
def sha256(string):
	shaSignature = \
		hashlib.sha256(string.encode()).hexdigest()
	return shaSignature

# MAIN
# We read the input
message = readInput()

print(sha256(message))

file = open("output.txt", "w")

file.write(message)