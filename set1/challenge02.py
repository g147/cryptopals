# Fixed XOR

from binascii import unhexlify, hexlify

def fixed_xor(hexInputA, hexInputB):
    hexInputA = unhexlify(hexInputA)
    hexInputB = unhexlify(hexInputB)
    return hexlify(bytes([ x^y for (x,y) in zip(hexInputA, hexInputB)])).decode()

def main():
    print(fixedXor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'))

if __name__ == '__main__':
    main()
