#!/bin/env python3
# cryptopals 11
# An ECB/CBC detection oracle

from cplib import aes_cbc, blocklify
from random import randint, getrandbits

def get_random_16_bytes():
    return bytes(getrandbits(8) for _ in range(16))

def random_pend(bstring):
    rand_p = bytes(getrandbits(8) for _ in range(randint(5,10)))
    rand_a = bytes(getrandbits(8) for _ in range(randint(5,10)))
    return rand_p + bstring + rand_a

def encryption_oracle(bstring):
    if has_douplicate_blocks(bstring):
        return "ecb"
    else:
        return "cbc"

def has_douplicate_blocks(bstring, size=16):
    blocks = blocklify(bstring, size)
    return not len(set(blocks)) == len(blocks)


def aes_ecb(key, secret):
    from Crypto.Cipher import AES
    cipher = AES.new(key, AES.MODE_ECB)
    from cplib import pad
    return cipher.encrypt(pad(secret))

def random_encrypt(secret):
    key = get_random_16_bytes()
    if randint(0,1):
        ivec = get_random_16_bytes()
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
