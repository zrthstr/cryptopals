#!/bin/env python3
# cryptopals 12
# Byte-at-a-time ECB decryption (Simple)

from base64 import standard_b64decode
from cplib import rand16bytes, aes_ecb, encryption_oracle, has_duplicate_blocks, pad

base_to_append = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"""

def chk_block_size():
    key = rand16bytes()
    for s in range(24 * 3 - 1):
        if has_duplicate_blocks(aes_ecb(key, bytes( s * "a", 'ascii'))):
            if s >= 24 * 2:
                return 24
            if s >= 16 * 2:
                return 16
            return 8


def main():
    assert 16 == chk_block_size()
    block_size = 16
        
    secret_key = rand16bytes() 
    recovered_plaintext = bytes()
    #unknown_plaintext = standard_b64decode(base_to_append)
    unknown_plaintext = bytes("0123456789ABCDEF", "ascii")
    #unknown_plaintext = bytes("123456789abcdef0123456789ABCDEF", "ascii")

    for c in range(1, len(unknown_plaintext) + 1):
        cc = c
        if cc > 15:
            cc -= 16
        print("CC", cc)

        known_plaintext = [pad( bytes(chr(x), 'ascii') + recovered_plaintext) for x in range(128)]
        len_pad = len(known_plaintext[0] + unknown_plaintext) % block_size + cc
        pading = bytes("B" * len_pad, 'ascii')

        for this_known_plaintext in known_plaintext:
            to_crypt = this_known_plaintext + pading + unknown_plaintext
            if has_duplicate_blocks(aes_ecb(secret_key, to_crypt)):
                recovered_plaintext = bytes(chr(this_known_plaintext[0]), 'ascii') + recovered_plaintext
                print(">>>> rec_key:", recovered_plaintext)
                break
        else:
            print("did not recover key, quitting")
            break


if __name__ == "__main__":
    main()
