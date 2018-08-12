#!/bin/env python3
# cryptopals 1.4
# Detect single-character XOR

from cplib import freq_analis, single_byte_xor
from binascii import unhexlify

def main():
    
    keyspace = range(256)
    with open("4.txt") as f:
        inp = f.read().splitlines()

    best_score = 0
    best_key = ""
    best_secret = ""

    for i in inp:
        i = bytes.fromhex(i)
        for key in keyspace:
            score = freq_analis(unhexlify(single_byte_xor(key, i)))
            if score > best_score:
                best_score = score
                best_key = key
                best_secret = unhexlify(single_byte_xor(key, i))


    print(best_score, best_key, best_secret)


if __name__ == "__main__":
    main()
