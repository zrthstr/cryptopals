#!/bin/env python3
# cryptopals 2.2
# Implement CBC mode

from base64 import standard_b64decode
from cplib import aes_cbc


def main():

    with open("10.txt") as f:
        inp = standard_b64decode("".join(f.read().splitlines()))

    ivec = bytearray(chr(0)*16, "ascii")
    key = bytes("YELLOW SUBMARINE", "ascii")
    print(aes_cbc(ivec, key, inp))


if __name__ == "__main__":
    main()
