import sys
import hashlib

def getKey(keyString, round):
	key = keyString[round*8:(round+1)*8]
	return key


def sha256(string):
	sha_signature = \
		hashlib.sha256(string.encode()).hexdigest()
	return sha_signature

#main
password = input("password: ")

keyString = sha256(password)
keyString += sha256(keyString)

for round in range(16):
	key = getKey(keyString, round)
	print (key)