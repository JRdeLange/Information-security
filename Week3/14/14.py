import sys

def modInverse(m, n):
	m = m % n; 
	for x in range(1, n) : 
		if ((m * x) % n == 1) : 
			return x

def addPoint(x1, y1, x2, y2, mod):
	if x1 == 0 and y1 == 0:
		return x2, y2
	l = ((y2 - y1) * modInverse((x2 - x1), mod)) % mod
	x3 = (pow(l, 2) - x1 - x2) % mod
	y3 = (l*x1 - l*x3 - y1) % mod
	return x3, y3
		
def doublePoint(x1, y1, a, mod):
	l = (3*pow(x1, 2) + a) * modInverse(2*y1, mod) % mod
	x3 = (pow(l, 2) - x1 - x1) % mod
	y3 = (l*x1 - l*x3 - y1) % mod
	return x3, y3

# all intitial values
a = 6
N = 197
X1 = 3
Y1 = 9
m = 19

# calculate b (= 36)
b = pow(Y1, 2) - pow(X1, 3) - a*X1


# check for the length of the binary representation of m
pwrOfTwo = 0
while pow(2, pwrOfTwo) < m:
	pwrOfTwo = pwrOfTwo + 1

# calculate (Xm, Ym)
Xm = 0
Ym = 0
for i in range(0,pwrOfTwo+1):
	if (m>>i & 1) == 1:
		Xm, Ym = addPoint(Xm, Ym, X1, Y1, N)
	X1, Y1 = doublePoint(X1, Y1, a, N)

print (Xm, Ym)
