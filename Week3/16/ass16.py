import sys
import hashlib
import base64

# The feistel function performs the encoding for a single
# round. For each set of 16 bytes we divide it into a left
# and right part. The right part becomes the left part of
# the next itteration, and the left part XOR the key and 
# the right part, becomes the right part of the next 
# itteration.
def feistel(key, message):
	encodedMessage = []
	for part in range(int(len(message)/16)):
		toEncode = message[part*16:(part+1)*16]

		left = toEncode[0:8]
		right = toEncode[8:16]

		newLeft = right
		newRight = []

		for enum in range(8):
			newRight.append(left[enum] ^ key[enum] ^ right[enum])

		encodedMessage.extend(newLeft + newRight)
	return encodedMessage

# The key schedule reads eight characters from the keystring
# each round and turns these into 4 ints, interpreting them
# as hexadecimal values.
def keySchedule(keyString, round):
	preKey = keyString[round*16:(round+1)*16]
	key = []

	for enum in range(8):
		key.append(preKey[enum*2]+preKey[enum*2+1])
		key[enum] = int(key[enum],16)

	return key

# This function will read the input via stdin, as bytes
# converting and returning the bytes as a list of ints.
def readInput():
	# We read the bitestream from stdin
	message = sys.stdin.buffer.read()

	# We turn the bytestring into an array of ints
	# removing the initialization vector which are 
	# the first 16 bytes
	message = list(message)[16:]

	return message

#This function return the SHA256 hash of its input
def sha256(string):
	shaSignature = \
		hashlib.sha256(string.encode()).hexdigest()
	return shaSignature

# MAIN
password = "(34,185)"

# We generate our key schedule by taking the SHA256 hash
# of the point
keyString = sha256(password)

# We read the input
message = readInput()

# We pad the message
if (len(message) % 16) == 0:
	padding = 16;
else:
	padding = 16 - (len(message) % 16)

for x in range(padding):
	message.append(padding)

# We encode for 4 rounds. Generating a key according to the
# keyschedule and encoding using the feistel function.
for round in range(4):
	key = keySchedule(keyString, round)
	message = feistel(key, message)

# We change the output back into bytes
message = bytearray(message)

print(message)

# We write the output to std:out
#sys.stdout.buffer.write(message)