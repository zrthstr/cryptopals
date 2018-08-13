#!/bin/env python3
# cryptopals 1.7
# AES in ECB mode

#from cplib import hex_to_base64

from Crypto.Cipher import AES
from base64 import standard_b64decode

def main():

    with open("7.txt") as f:
        inp = standard_b64decode("".join(f.read().splitlines()))

    key = bytes("YELLOW SUBMARINE", encoding="ascii")
    cipher = AES.new(key, AES.MODE_ECB)

    msg = cipher.decrypt(inp)

    print(msg)


if __name__ == "__main__":
    main()
