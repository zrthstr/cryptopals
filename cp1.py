#!/bin/env python3
# cryptopals 1.1
# Convert hex to base64 

from cplib import hex_to_base64


str_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
correct = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def main():
    base = hex_to_base64(str_in)
    print("in: %s\nout: %s \ncorret: %s" %(str_in, base, correct))


if __name__ == "__main__":
    main()
