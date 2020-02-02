# AES in ECB mode

from base64 import b64decode
from Crypto.Cipher import AES

def main():
    key = b'YELLOW SUBMARINE'
    encrypted = b64decode(open('data/challenge07.txt').read())
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted)
    print(decrypted.decode())

if __name__ == "__main__":
    main()