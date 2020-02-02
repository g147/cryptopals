def main():
    messages = open('data/challenge05.txt').readlines()
    key = "ICE"     
    for text in messages:
        cipher = repeating_key_xor(text, key)
        print (cipher.hex())

def repeating_key_xor(message, key):
    i=0
    cipher=b''
    key=key.encode()
    message=message.encode()
    for byte in message:
        cipher += bytes([byte^key[i]])
        if len(key)==(i+1):
            i=0
        else:
            i+=1
    return cipher

if __name__ == "__main__":
    main()