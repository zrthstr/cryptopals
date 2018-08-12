#!/bin/env python3
# cryptopals 0.0
# Some Name

import base64
from cplib import hamming

def test_haming():
    a = bytes("this is a test", encoding="ascii")
    b = bytes("wokka wokka!!!", encoding="ascii")
    d = hamming(a,b)
    print("hamming syays :", d)


def n_hamming(a,b):
    return hamming(a,b) / len(a)


def find_key_size(mini, maxi, secret):
    assert mini < maxi < len(secret)
    assert maxi * 4 < len(secret)

    opti_key_len = 0
    mini_n_ham = 1000

    key_range = range(mini, maxi + 1)
    for key_len in key_range:
        c = 0
        end = 0
        ham = []
        while True: 
            start = c * key_len
            end = start + key_len 
            if end > len(secret) - key_len:
                break
            #print(start, end, start + key_len, end + key_len)
            ham.append(n_hamming(secret[start:end], secret[start+key_len:end+key_len]))
            c += 1    
        n_ham = sum(ham) / len(ham)    
        #print(n_ham, ham)

        if n_ham < mini_n_ham:
            opti_key_len = key_len
            mini_n_ham = n_ham


    print("opti_key_len: ",opti_key_len)
    print("mini_n_ham: ", mini_n_ham)

def main():

    with open("6.txt") as f:
        inp = "".join(f.read().splitlines())

    inp = base64.standard_b64decode(inp)

    print(inp)
    find_key_size(4,40,inp)


    str_in = ""
    correct = ""
    out = ""
    print("in: %s\nout: %s \ncorret: %s" %(str_in, out, correct))


if __name__ == "__main__":
    main()
