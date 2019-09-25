import sys

#get input, remove \n
text = list(sys.stdin.readline())
text.pop()
key1 = list(sys.stdin.readline())
key1.pop()
key2 = list(sys.stdin.readline())

#transform to numbers
for x in range(0, len(text)):
	text[x] = ord(text[x])
	key1[x] = ord(key1[x])
	key2[x] = ord(key2[x])

encrypt = []
decrypt = []

for x in range(0, len(text)):
	encrypt.append(text[x] ^ key1[x])
	decrypt.append(encrypt[x] ^ key2[x])

decryptstring = ""
for x in range(0, len(text)):
	decryptstring = decryptstring + chr(decrypt[x])

print (encrypt)
print (decryptstring)