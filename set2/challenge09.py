# Implement PKCS#7 padding

from base64 import b64decode
from Crypto.Util.Padding import pad

def main():
    data = b'YELLOW SUBMARINE'
    size = 20
    print(pad(data, size))

if __name__ == "__main__":
    main()