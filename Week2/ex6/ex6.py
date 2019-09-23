import sys

knapsack = [2, 5, 9, 18, 40, 84, 175, 345, 712, 1400, 2840, 5777, 12032, 25323, 50213, 103421]

#get sum of all
total = 0
for x in knapsack:
	total=total+x

#choose n and m
n = total + 1075 # = 203471
m = 64
print ("n = " + str(n) + ", m = " + str(m))

#get public key
public = list()
for x in range(0,len(knapsack)):
	public.append(m*knapsack[x]%n)

#modular inverse
m = m % n; 
for x in range(1, n) : 
    if ((m * x) % n == 1) : 
        inverse = x
        break

#get input
line = sys.stdin.readline()
line = line.split()

#parse input into numbers
encrypted = []
for x in range(0,len(line)):
	encrypted.append(int(line[x]))

#perform needed calculations with the inverse
inverted = []
for x in encrypted:
	inverted.append(x*inverse%n)

#use knapsack to decrypt the inverted numbers
decrypted = []
for x in inverted:
	num = x
	block = 0
	for y in range(len(knapsack)-1, -1, -1):
		block = block * 2
		if num >= knapsack[y]:
			num = num - knapsack[y]
			block = block + 1 
	decrypted.append(block)
			
#decrypted[0]        - original
#decrypted[0] >> 8   - leftmost 8 bits
#decrypted[0] & 255  - rightmost 8 bits

#split the blocks and enter into string
decyphered = ""
for x in decrypted:
	decyphered = decyphered + chr(x >> 8)
	decyphered = decyphered + chr(x & 255)
	
	
print (decyphered)