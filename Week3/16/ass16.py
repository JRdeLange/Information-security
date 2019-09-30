import sys
import hashlib

# The feistel function performs the encoding for a single
# round. For each set of 8 bytes we divide it into a left
# and right part. The right part becomes the left part of
# the next itteration, and the left part XOR the key 
# becomes the right part of the next itteration.
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

# This function will read and save all of the lines entered
# after being called until EOF has been reached. It then 
# returns this as one long string.
def readInput():
	message = []

	while True:
		line = sys.stdin.readline()
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
password = input("Shared ECC point: ")

# We generate our key schedule by taking the SHA256 hash
# of the point
keyString = sha256(password)

# We read the input
message = readInput()

# We change the input characters to ints so we can use the ^ opperator.
for element in range(len(message)):
	message[element] = ord(message[element])

# Pad the message
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

# We change the message back into character for our output.
for element in range(len(message)):
	message[element] = chr(message[element])

print(''.join(message))