import sys

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
    return i, j, s[t]
    
if __name__ == '__main__':
    text = sys.stdin.buffer.read(None)
    key = "2019"
    stream = initialise(key)
    i = j = 0
    # Ignore first 256 bytes
    for x in range(256):
        i, j, temp = keyStreamByte(i, j, stream)
        
    # Encryption or decryption, depending on whether the text is plaintext or cipher text.
    final_text = ""
    for x in range(0, len(text)):
        i, j, streamByte = keyStreamByte(i, j, stream)
        # Note: although this program can be used to both encrypt and decrypt
        # RC4, it should be noted that when encrypting the output will not be
        # binary (but unicode instead). This is because of the chr() function 
        # which is implemented to make decrypted text human-readable.
        # This does not affect encryption/decryption in any way.
        final_text += chr(text[x] ^ streamByte) # xor and convert to unicode.
    print(final_text)
