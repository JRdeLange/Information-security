#Information security Assignment 1 Exercise 2

print("""
Usage: substitution [-o] [-d] mapping \n
Where: \n
-o: keep non-letters as is, honor letter casing\n
-d: decrypt
mapping: 26 letter char-mapping or an int-value\n 
\n
En/Decrypts stdin to stdout. Only letters are \n
encrypted, all other characters are silently\n
ignored, unless -o was specified, in which case\n
they are used as-is. When -o is specified, letter\n
casing is honored, otherwise all letters are\n
converted to lower-case letters. Use an int-value\n
to do a letter shift (% 26, 0: a = a)Shift 3 is\n
the classical Caesar encryption
""")
command = input()

array = 'abcdefghijklmnopqrstuvwxyz'

key = command[len(command)-1]

if ord(key) > 47 and ord(key) < 58:
	key = int(key)
	array = array[-key:]+array[:-key]
	key = ['abcdefghijklmnopqrstuvwxyz', array]
	remainingLength = len(command)
	print(key)
else:
	key = ['abcdefghijklmnopqrstuvwxyz', command[len(command)-26:len(command)]]
	remainingLength = len(command)-25

print(key)

nonLetters = 'discard'
mode = 'e'

if command[remainingLength-4] == "-":

	if command[remainingLength-3] == 'd':
		mode = 'd'
		if command[remainingLength-7] == "-" and command[remainingLength-6] == 'o':
			nonLetters = 'keep'
			text = command[0:remainingLength-8]
		else:
			text = command[0:remainingLength-5]

	elif command[remainingLength-3] == 'o':
		nonLetters = 'keep'
		text = command[0:len(command)-5]
	else:
		text = command[0:len(command)-2]

else:
	text = command[0:len(command)-2]

if mode == "d":
	temp = key[0]
	key[0] = key[1]
	key[1] = temp

encodedText = ""

for symbol in text:

	if symbol.isalpha():

		if symbol.isupper():
			newSymbol = chr(ord(symbol) + 32)
			newSymbol = key[1][key[0].find(newSymbol)]
			if nonLetters == "keep":
				newSymbol = chr(ord(newSymbol) - 32)

		if symbol.islower():
			newSymbol = key[1][key[0].find(symbol)]

		encodedText += newSymbol

	elif nonLetters == "keep":
		encodedText += symbol


print('Result:\n' + encodedText)