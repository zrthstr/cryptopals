#!/bin/env python3
# cryptopals 2.2
# Implement CBC mode

from cplib import rkey_xor, pad
from Crypto.Cipher import AES
from base64 import standard_b64decode
from binascii import unhexlify


str_in = ""
correct = ""

def blocklify(to_split, size):
    assert size > 0
    return [to_split[i:i+size] for i in range(0, len(to_split), size)]


def main():

    with open("10.txt") as f:
        inp = standard_b64decode("".join(f.read().splitlines()))

    key = bytes("YELLOW SUBMARINE", "ascii")
    cipher = AES.new(key, AES.MODE_ECB)

    out = ""
    print("in: %s\nout: %s \ncorret: %s" %(str_in, out, correct))

    first_iv = bytearray(chr(0)*16, "ascii")
    first_block = inp[0:16]    
    out = rkey_xor(first_iv, first_block)
    #out = unhexlify(out)
    print(type(out))
    msg = cipher.decrypt(out)
    print("first_iv: ", first_iv, "first_block: ", first_block, "out: ", out, "msg: ", msg)


    blocks = blocklify(inp, 16)
    blocks[-1] = pad(blocks[-1])   
    
    iv = first_iv
    for block in blocks:
        out = rkey_xor(iv, block)
        cipher = AES.new(key, AES.MODE_ECB)
        out = cipher.decrypt(out)
        print(out)
        iv = msg

    #print(slices)    

if __name__ == "__main__":
    main()
