#!/bin/env python3
# cryptopals 11
# An ECB/CBC detection oracle

from cplib import aes_cbc, aes_ecb, blocklify, rand16bytes, has_duplicate_blocks, encryption_oracle
from random import randint, getrandbits


def random_pend(bstring):
    rand_p = bytes(getrandbits(8) for _ in range(randint(5,10)))
    rand_a = bytes(getrandbits(8) for _ in range(randint(5,10)))
    return rand_p + bstring + rand_a


def random_encrypt(secret):
    key = rand16bytes()
    if randint(0,1):
        ivec = rand16bytes()
        return "cbc", aes_cbc(ivec, key, secret)
    else:
        return "ecb", aes_ecb(key, secret)
    

def main():

    rounds = 1000

    with open("gangster_ipsum.txt") as f:
       inp = "".join(f.readlines())
    inp = bytes(inp, encoding="ascii")

    orcale_count = 0
    for r in range(rounds):
        mode, o = random_encrypt(random_pend(inp))
        oo = encryption_oracle(o)
        if mode == oo:
            orcale_count += 1
    print("orcale_count: %d from %d" %(orcale_count, rounds))

if __name__ == "__main__":
    main()
