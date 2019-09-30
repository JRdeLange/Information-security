import sys

def modInverse(m, n):
	m = m % n; 
	for x in range(1, n) : 
		if ((m * x) % n == 1) : 
			return x

p = 31
q = 41


N = 31 * 41			# = 1271
phi = (p-1)*(q-1)	# = 1200

print (N, phi)

e = 7

#private key
d = modInverse(e, phi)

print (d)

K = 42

C = pow(K, e) % N

print (C)
print (pow(C, d) % N)
