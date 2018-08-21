#!/bin/env python3
# cryptopals 2.1
# Implement PKCS#7 padding

from cplib import pad

def test():
    test = [ (c + 1) * chr(x + ord("a") )  for c, x in enumerate(range(26))]
    print(test)

    for t in test:
        print("in  : ", bytes(t, "ascii"))
        print("out : ", pad(bytes(t, "ascii")), "\n")


def main():

    #test()

    test1 = bytes("YELLOW SUBMARINE", "ascii")
    print("test1: ", test1 )
    print("test1: ", pad(test1, pad_to=20))

if __name__ == "__main__":
    main()
