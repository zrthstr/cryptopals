#!/bin/env python3
# cryptopals 1.5
# Implement repeating-key XOR

from cplib import rkey_xor
from binascii import hexlify

str_in = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

str_correct = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226\
324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302\
e27282f" 


def main():
    key = bytearray("ICE", "ascii")
    str_out = hexlify(rkey_xor(key, str_in ))
    print("in: %s\nstr_out: %s\nstr_correct: %s" % (str_in, str_out, str_correct))
    #print( rkey_xor(str.encode("ICE"), str.encode(str_in[1])))
if __name__ == "__main__":
    main()
