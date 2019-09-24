import sys
import hashlib

#This function return the SHA256 hash of its input
def sha256(string):
	shaSignature = \
		hashlib.sha256(string.encode()).hexdigest()
	return shaSignature

# MAIN
words = open(r"nsa.spy.txt","r")

words.read()
# We generate SHA256 hash of the input
#wordHash = sha256(words)
#print(wordHash)
#wordHash = sha256(wordHash)
#print(wordHash)