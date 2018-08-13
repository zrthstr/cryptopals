#!/bin/env python3
# cryptopals 0.0
# Some Name

import base64
from binascii import unhexlify
from cplib import hamming, find_key_size, find_single_byte_key, rkey_xor


def test_haming():
    test_a = bytes("this is a test", encoding="ascii")
    test_b = bytes("wokka wokka!!!", encoding="ascii")
    test_d = hamming(test_a, test_b)
    print("hamming syays :", test_d)

def main():

    with open("6.txt") as f:
        inp = "".join(f.read().splitlines())

    inp = base64.standard_b64decode(inp)
    key_size = find_key_size(4, 41, inp)
    key = bytes([find_single_byte_key(inp[k::key_size]) for k in range(key_size)])

    print("key_size: %s" % key_size)
    print("key: %s" % key)
    print(unhexlify(rkey_xor(key, inp)))


if __name__ == "__main__":
    main()
