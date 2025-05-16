def hash(s, k=31, p=2**64):
    h = 0
    K = [k**i for i in range(len(s))]
    for i in range(len(s)):
        h += (K[i] * (ord(s[i]) - ord('a'))) % p
    return h

def reversed_hash(s, k=31, p=2**64):
    h = 0
    K = [k**(len(s) - i - 1) for i in range(len(s))]
    for i in range(len(s)):
        h += (K[i] * (ord(s[i]) - ord('a'))) % p
    return h
