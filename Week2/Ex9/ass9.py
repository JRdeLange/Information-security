import sys
import hashlib

# The feistel function performs the encoding for a single
# round. For each set of 8 bytes we divide it into a left
# and right part. The right part becomes the left part of
# the next itteration, and the left part XOR the key 
# becomes the right part of the next itteration.
def feistel(key, message):
	encodedMessage = []
	for part in range(int(len(message)/8)):
		toEncode = message[part*8:(part+1)*8]

		left = toEncode[0:4]
		right = toEncode[4:8]

		newLeft = right
		newRight = []

		for enum in range(4):
			newRight.append(left[enum] ^ key[enum])

		encodedMessage.extend(newLeft + newRight)

	return encodedMessage

# The key schedule reads eight characters from the keystring
# each round and turns these into 4 ints, interpreting them
# as hexadecimal values.
def keySchedule(keyString, round):
	preKey = keyString[round*8:(round+1)*8]
	key = []

	for enum in range(4):
		key.append(preKey[enum*2]+preKey[enum*2+1])
		key[enum] = int(key[enum],16)

	return key

# This function will read and save all of the lines entered
# after being called until EOF has been reached. It then 
# returns this as one long string.
def readFile():
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
password = input("password(s): ")

# We generate our key schedule by taking the SHA256 hash
# of the password(s) and appending the SHA256 hash of this
# SHA256 hash to it.
keyString = sha256(password)
keyString += sha256(keyString)

# We read the input
message = readFile()

# We change the input characters to ints for the next step.
for element in range(len(message)):
	message[element] = ord(message[element])

# We pad the input so that it is divisible by 8. If it is
# already divisible by 8 we pad by 8.
if (len(message) % 8) == 0:
	padding = 8
else:
	padding = 8 - (len(message) % 8)

for x in range(padding):
	message.append(0)

# We encode for 16 rounds. Generating a key according to the
# keyschedule and encoding using the feistel function.
for round in range(16):
	key = keySchedule(keyString, round)
	message = feistel(key, message)

# We change the message back into character for our output.
for element in range(len(message)):
	message[element] = chr(message[element])

message = ''.join(message)

print(sha256(message))

file = open("output.txt", "w")

file.write(message)