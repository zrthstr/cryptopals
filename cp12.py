#!/bin/env python3
# cryptopals 12
# Byte-at-a-time ECB decryption (Simple)

from base64 import standard_b64decode
from cplib import rand16bytes, aes_ecb, encryption_oracle, has_duplicate_blocks

base_to_append = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK"""

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
        
    #u_plain = standard_b64decode(base_to_append)
    u_plain = bytes("0123456789ABCDEF", "ascii")
    secret_key = rand16bytes() 
    rec_key = bytes()

    print("u_plain has len: ", len(u_plain))


    k_plain = [bytes(chr(x), 'ascii') + bytes(chr(15), 'ascii') * 15 for x in range(128)]
    len_pad = len(k_plain[0] + u_plain) % 16 + 1
    pad = bytes("B" * len_pad, 'ascii')
    for kk_plain in k_plain:
        c = kk_plain + pad + u_plain
        co = aes_ecb(secret_key, c)
        if has_duplicate_blocks(co):
            rec_key = bytes(chr(kk_plain[0]), 'ascii') + rec_key
            print(">>>> rec_key:", rec_key)

    k_plain = [bytes(chr(x), 'ascii') + rec_key  + bytes(chr(14), 'ascii') * 14 for x in range(128)]
    len_pad = len(k_plain[0] + u_plain) % 16 + 2
    pad = bytes("B" * len_pad, 'ascii')
    for kk_plain in k_plain:
        c = kk_plain + pad + u_plain
        co = aes_ecb(secret_key, c)
        if has_duplicate_blocks(co):
            rec_key = bytes(chr(kk_plain[0]), 'ascii') + rec_key
            print(">>>> rec_key:", rec_key)

    k_plain = [bytes(chr(x), 'ascii') + rec_key  + bytes(chr(13), 'ascii') * 13 for x in range(128)]
    len_pad = len(k_plain[0] + u_plain) % 16 + 3
    pad = bytes("B" * len_pad, 'ascii')
    for kk_plain in k_plain:
        c = kk_plain + pad + u_plain
        co = aes_ecb(secret_key, c)
        if has_duplicate_blocks(co):
            rec_key = bytes(chr(kk_plain[0]), 'ascii') + rec_key
            print(">>>> rec_key:", rec_key)

if __name__ == "__main__":
    main()
