import sys

knapsack = [1,4,7,10,13,15,28,34,57,59,64,75,85,109,123,137]

#get sum of all
total = 0
for x in knapsack:
	total=total+x

#choose n and m
n = total + 174 # = 995
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

numbers = []
for x in range(0,len(line)):
	numbers.append(int(line[x]))

for x in numbers:
	print (bin(x))




'''
frame = bytearray()
for x in line:
	frame.append(int(x))

print (bin(frame[1] & 0b11000000))

q = 0b00110101
print (q >> 9 & 0b1)

print(bin(q))



test = 0b001000
print (bin(test))
print (test)
test = test << 8
print (bin(test))
print (test)
'''