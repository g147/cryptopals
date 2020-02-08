# Convert hex to base64

from binascii import unhexlify, b2a_base64

def hex2base64(hexInput):
    return b2a_base64(unhexlify(hexInput)).decode()

def main():
    print(hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

if __name__ == '__main__':
    main()