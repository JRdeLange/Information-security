import sys
import hashlib
import hmac
import base64
import array

if __name__ == '__main__':
    security_file = sys.stdin.buffer.read(None)
    key = "Nathan-vanBeelen" # my name

    # Convert string to bytearray
    b = bytearray()
    b.extend(key.encode())

    # Use the python hmac library (based on RFC 2104).
    security_hash = hmac.digest(b, security_file, hashlib.sha256)

    # Convert hash to base64 to make it readable.
    print(base64.b64encode(security_hash))
