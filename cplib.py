
from base64 import standard_b64encode
from binascii import hexlify
from collections import Counter



def hex_to_base64(h):
    h = bytes.fromhex(h)
    return standard_b64encode(h)


def fixed_xor(a,b):
    if not len(a) == len(b):
        raise ValueError("len of values to xor is not the same")

    out = [a[x] ^ b[x] for x in range(len(a))]
    return hexlify(bytearray(out))


def single_byte_xor(key, string):
    out = [x ^ key for x in string]
    return hexlify(bytearray(out))


def rkey_xor(rkey, string):
    multi = len(string) // len(rkey) + 1
    rkey = rkey * multi
    out = [rkey[x] ^ string[x] for x in range(len(string))]
    return hexlify(bytearray(out))



char_freq_en = {
        " ": 14.45, ## this one is added by me, the rest from wiki..
        "e": 12.7,
        "t": 9.0,
        "a": 8.1,
        "o": 7.5,
        "i": 6.9,
        "n": 6.7,
        "s": 6.3,
        "h": 6.1,
        "r": 6.0,
        "d": 4.3,
        "i": 4.0,
        "c": 2.8,
        "u": 2.8,
        "m": 2.4,
        "w": 2.7,
        "f": 2.2,
        "g": 2.0,
        "y": 2.0,
        "p": 1.9,
        "b": 1.5,
        "v": 1.0,
        }


def freq_analis(string, freq_table=char_freq_en):
    count = Counter(string)
    return sum([ v * freq_table[chr(k)] for k, v in count.items() if chr(k) in freq_table ])



