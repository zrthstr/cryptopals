#!/bin/env python3
# cryptopals 1.3
# Single-byte XOR cipher


from cplib import single_byte_xor, freq_analis
import binascii


str_in = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def main():
    hex_in = bytes.fromhex(str_in)
    all_out = [single_byte_xor(key, hex_in) for key in range(256)]


    max_freq = 0
    key = 0

    for c, o in enumerate(all_out):
        freq = freq_analis(binascii.unhexlify(o))
        if freq > max_freq:
            max_freq = freq
            key = c

    print("secret: ", binascii.unhexlify(all_out[key]))


if __name__ == "__main__":
    main()
