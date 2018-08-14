#!/bin/env python3
# cryptopals 2.1
# Implement PKCS#7 padding

#from cplib import hex_to_base64

def pad(bstring, scheme="PKCS#7", pad_to=16):
    assert scheme == "PKCS#7"
    pad = pad_to - len(bstring) % pad_to
    padding = chr(pad) * pad
    return bstring + bytes(padding, "ascii")


def main():
    test = [ (c + 1) * chr(x + ord("a") )  for c, x in enumerate(range(26))]
    print(test)

    for t in test:
        print("in  : ", bytes(t, "ascii"))
        print("out : ", pad(bytes(t, "ascii")), "\n")

    test1 = bytes("YELLOW SUBMARINE", "ascii")
    print("test1: ", test1 )
    print("test1: ", pad(test1, pad_to=20))

if __name__ == "__main__":
    main()
