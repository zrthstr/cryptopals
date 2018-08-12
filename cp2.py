#!/bin/env python3
# cryptopals 1.2
# Fixed XOR

from cplib import fixed_xor


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

correct = b"746865206b696420646f6e277420706c6179"


def main():
    result = fixed_xor(bytes.fromhex(a), bytes.fromhex(b))

    print("in: %s\nin: %s\nresult: %s \ncorret: %s" %(a, b, result, correct))


if __name__ == "__main__":
    main()
