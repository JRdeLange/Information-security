import sys
import hashlib

#This function return the SHA256 hash of its input
def sha256(string):
	shaSignature = \
		hashlib.sha256(string.encode()).hexdigest()
	return shaSignature

def readFile():
	message = []

	while True:
		line = sys.stdin.readline()
		if line == '':
			break
		message += line
	#message.pop(len(message)-1)

	return message

# MAIN
words = (''.join(readFile()))

# We generate SHA256 hash of the input
wordHash = sha256(words)
print(wordHash)
wordHash = sha256(wordHash)
print(wordHash)