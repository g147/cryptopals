# AES in ECB mode

from base64 import b64decode
from Crypto.Cipher import AES

def aes_ecb_decrypt(key, encrypted):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted).decode()
    return decrypted

def main():
    key = b'YELLOW SUBMARINE'
    encrypted = b64decode(open('data/challenge07.txt').read())
    print(aes_ecb_decrypt(key,encrypted))

if __name__ == "__main__":
    main()