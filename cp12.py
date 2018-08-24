#!/bin/env python3
# cryptopals 12
# Byte-at-a-time ECB decryption (Simple)

from base64 import standard_b64decode
from cplib import aes_ecb, has_duplicate_blocks, pad, randbytes, chk_block_size

base_to_append = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"""


def main():
    block_size = chk_block_size()
    assert block_size == 16
    
    secret_key = randbytes(block_size) 
    recovered_plaintext = randbytes(block_size -1)
    unknown_plaintext = standard_b64decode(base_to_append)
    payload = recovered_plaintext + unknown_plaintext
    padding = randbytes((len(unknown_plaintext) // block_size + 1) * block_size) 

    for _ in range(len(unknown_plaintext)):
        for this in range(0,128):
            this = bytes(chr(this), 'ascii')
            to_crypt = recovered_plaintext[-(block_size-1):] + this + padding + payload
            if has_duplicate_blocks(aes_ecb(secret_key, to_crypt)):
                recovered_plaintext += this
                padding = padding[:-1]
                break

    print("Recovered plaintext:", recovered_plaintext[block_size-1:])

if __name__ == "__main__":
    main()
