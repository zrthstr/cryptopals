#!/bin/env python3
# cryptopals 0.0
# Detect AES in ECB mode

from cplib import find_single_byte_key, rkey_xor, n_hamming
from binascii import unhexlify


def search_ecb_by_hamming(lines):
    key_size = 16
    scores = []
    for line in lines:
        score = []
        for c in range((len(line) // 16) - 1):
            start = c * key_size
            end = c * key_size + key_size
            nh = n_hamming(line[start:end], line[start+key_size:end+key_size])
            score.append(nh)
        scores.append( sum(score) / len(score))
        #print(sub, nh)
        #key = bytes([find_single_byte_key(line[k::key_size]) for k in range(key_size)])
        #print("key_size: %s" % key_size)
        #print("key: %s" % key)
        #print(unhexlify(rkey_xor(key, line)))

    #print(scores) 
    #print(min(scores))
    #print(scores.index(min(scores)))
    return scores.index(min(scores))


def detect_ecb_by_doublicat_blocks(lines):
    key_size = 16
    ecb = []
 
    for c, line in enumerate(lines):
        blocks = [line[i:i+16] for i in range(0, len(line), 16)]    
        if not len(blocks) == len(set(blocks)):
            ecb.append(c)

    return ecb


def main():
    with open("8.txt") as f:
        lines = f.read().splitlines()
    lines = [ bytes.fromhex(l) for l in lines]

    #print(lines)
    ecb = search_ecb_by_hamming(lines)
    print(ecb)

    ecb = detect_ecb_by_doublicat_blocks(lines)
    print(ecb)

if __name__ == "__main__":
    main()
