#!/bin/env python3
# cryptopals 12
# Byte-at-a-time ECB decryption (Simple)

from base64 import standard_b64decode
from cplib import rand16bytes, aes_ecb, encryption_oracle, has_duplicate_blocks, pad

base_to_append = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"""

#base_to_append = """Um9sbGiAodsahdohJSAOIJsjaiiAohoidhaAHispsiluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"""

def chk_block_size():
    key = rand16bytes()
    for s in range(24 * 3 - 1):
        if has_duplicate_blocks(aes_ecb(key, bytes( s * "a", 'ascii'))):
            if s >= 24 * 2:
                return 24
            if s >= 16 * 2:
                return 16
            return 8

from random import getrandbits
def randbytes(n):
    assert n > -1
    return bytes(getrandbits(8) for _ in range(n))
    

def main():
    block_size = chk_block_size()
    assert block_size == 16
    
    secret_key = rand16bytes() 
    recovered_plaintext = rand16bytes()[1:]
    recovered_plaintext2 = recovered_plaintext
    unknown_plaintext = standard_b64decode(base_to_append)
    padding = randbytes((len(unknown_plaintext) // block_size + 1) * block_size) 

    print(len(padding), padding)

    for _ in range(len(unknown_plaintext)):
        for this in range(0,128):
            this = bytes(chr(this), 'ascii')
        
            to_crypt = recovered_plaintext[-15:] + this + padding + recovered_plaintext2 + unknown_plaintext
            
            if has_duplicate_blocks(aes_ecb(secret_key, to_crypt)):
                recovered_plaintext += this
                print(">>>> foun new letter:", this, recovered_plaintext)
                break
        print(".", end="")
   
        padding = padding[:-1]

    print("Recovered plaintext seems to be: ", recovered_plaintext[block_size-1:])

if __name__ == "__main__":
    main()
