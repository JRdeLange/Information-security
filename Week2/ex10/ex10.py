# Initialisation
def initialise(key):
    # Convert the key
    K = [None] * len(key)
    for i in range(0, len(key)):
        K[i] = ord(key[i])
    s = [n for n in range(256)]
    k = [None] * 256
    for i in range(256):
        k[i] = K[i % len(key)]
    j = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        s[i], s[j] = s[j], s[i] # swap
    return s

def keyStreamByte(i, j, s):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i] # swap
    t = (s[i] + s[j]) % 256
    return s[t]
    
if __name__ == '__main__':
    text = "test"
    key = "2019"
    stream = initialise(key)
    i = j = 0
    # Ignore first 256 bytes
    for x in range(256):
        keyStreamByte(i, j, stream)
        
    # Encryption or decryption, depending on whether the text is plaintext or cipher text.
    for x in range(0, len(text)):
        streamByte = keyStreamByte(i, j, stream)
        print(ord(text[i]) ^ streamByte) # xor and print
