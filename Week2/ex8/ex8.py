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

for x in range(0, len(text)):
	encrypt[x] = (encrypt[x])
	decrypt[x] = decrypt[x] ^ key2[x]

print (encrypt)
print (decrypt)