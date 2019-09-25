# Initialisation
key = "2019"
s = [n for n in range(256)]
k = []
for i in range(256):
    k[i] = key[i % len(key)]
j = 0
for i in range(256):
    j = (j + s[i] + k[i]) % 256
    swap(s[i], s[j])

def keyStreamByte(i, j, s):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    swap(s[i], s[j])
    t = (s[i] + s[j]) % 256
    return s[t]

def swap(x, y):
    x, y = y, x
