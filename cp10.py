#!/bin/env python3
# cryptopals 2.2
# Implement CBC mode

from cplib import rkey_xor
from Crypto.Cipher import AES
from base64 import standard_b64decode


str_in = ""
correct = ""


def main():

    with open("10.txt") as f:
        inp = standard_b64decode("".join(f.read().splitlines()))

    cipher = AES.new(key, AES.MODE_ECB)

    out = ""
    print("in: %s\nout: %s \ncorret: %s" %(str_in, out, correct))

    first_iv = chr(0)*16
    first_block = cipher[:16]    

    out = rkey_xor(first_iv, first_block)
    print(out)


if __name__ == "__main__":
    main()
