
from base64 import standard_b64encode
from binascii import hexlify, unhexlify
from collections import Counter
from Crypto.Cipher import AES
from random import getrandbits


def hex_to_base64(h):
    h = bytes.fromhex(h)
    return standard_b64encode(h)


def encryption_oracle(bstring):
    if has_duplicate_blocks(bstring):
        return "ecb"
    else:
        return "cbc"


def has_duplicate_blocks(bstring, size=16):
    blocks = blocklify(bstring, size)
    return not len(set(blocks)) == len(blocks)


def fixed_xor(a,b):
    if not len(a) == len(b):
        raise ValueError("len of values to xor is not the same")

    out = [a[x] ^ b[x] for x in range(len(a))]
    return hexlify(bytearray(out))


def single_byte_xor(key, string):
    out = [x ^ key for x in string]
    return hexlify(bytearray(out))


#def rkey_xor(rkey, string):
#    multi = len(string) // len(rkey) + 1
#    rkey = rkey * multi
#    out = [rkey[x] ^ string[x] for x in range(len(string))]
#    return hexlify(bytearray(out))


def rkey_xor(rkey, string):
    multi = len(string) // len(rkey) + 1
    rkey = rkey * multi
    out = [rkey[x] ^ string[x] for x in range(len(string))]
    return bytes(out)



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


def hamming(a, b):
    if not len(a) == len(b):
        raise ValueError("len a not len b")
    return sum([ bin(a[x] ^ b[x]).count("1") for x in range(len(a))])


def n_hamming(a,b):
    return hamming(a,b) / len(a)

def find_single_byte_key(string):

    max_freq = 0
    key = 0

    all_xord = [single_byte_xor(key, string) for key in range(256)]
    for c, o in enumerate(all_xord):
        freq = freq_analis(unhexlify(o))
        if freq > max_freq:
            max_freq = freq
            key = c
    return key

def find_key_size(mini, maxi, secret):
    assert mini < maxi < len(secret)
    assert maxi * 4 < len(secret)

    opti_key_len = 0
    mini_n_ham = 1000

    key_range = range(mini, maxi + 1)
    for key_len in key_range:
        c = 0
        ham = []
        while True: 
            start = c * key_len
            end = start + key_len 
            if end > len(secret) - key_len:
                break
            ham.append(n_hamming(secret[start:end], secret[start+key_len:end+key_len]))
            c += 1    

        n_ham = sum(ham) / len(ham)    
        if n_ham < mini_n_ham:
            opti_key_len = key_len
            mini_n_ham = n_ham

    return opti_key_len

def pad(bstring, scheme="PKCS#7", pad_to=16):
    assert scheme == "PKCS#7"
    pad = pad_to - len(bstring) % pad_to
    if pad == pad_to:
        pad = 0
    padding = chr(pad) * pad
    return bstring + bytes(padding, "ascii")


def blocklify(to_split, size):
    assert size > 0
    return [to_split[i:i+size] for i in range(0, len(to_split), size)]


def aes_cbc(iv, key, secret):
    cipher = AES.new(key, AES.MODE_ECB)
    blocks = blocklify(secret, 16)
    blocks[-1] = pad(blocks[-1])

    out_blocks = bytes()
    for block in blocks:
        out = rkey_xor(iv,   cipher.decrypt(block))
        out_blocks += out
        iv = block
    return out_blocks


def aes_ecb(key, secret):
    from Crypto.Cipher import AES
    cipher = AES.new(key, AES.MODE_ECB)
    from cplib import pad
    return cipher.encrypt(pad(secret))


def rand16bytes():
    return bytes(getrandbits(8) for _ in range(16))

def randbytes(n):
    assert n > -1
    return bytes(getrandbits(8) for _ in range(n))

def chk_block_size():
    key = rand16bytes()
    for s in range(24 * 3 - 1):
        if has_duplicate_blocks(aes_ecb(key, bytes( s * "a", 'ascii'))):
            if s >= 24 * 2:
                return 24
            if s >= 16 * 2:
                return 16
            return 8
