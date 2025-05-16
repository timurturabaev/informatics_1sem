import cmath

def fft(x):
    n = len(x)
    if n == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    y = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + y[k] for k in range(n // 2)] + [even[k] - y[k] for k in range(n // 2)]

def invfft(x):
    n = len(x)
    if n == 1:
        return x
    even = invfft(x[0::2])
    odd = invfft(x[1::2])
    y = [cmath.exp(2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + y[k] for k in range(n // 2)] + [even[k] - y[k] for k in range(n // 2)]

def biba(a, b, m):
    maxmatches = 0
    trans = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    at = [trans[c] for c in a]
    bt = [trans[c] for c in b]
    for d in range(4):
        an = [1 if i == d else 0 for i in at]
        bn = [1 if i == d else 0 for i in bt]
        bn2=bn
        ffta = fft(an)
        fftb = fft(bn2[::-1])
        sp = [ffta[l] * fftb[l] for l in range(m)]
        obratno = invfft(sp)
        nuclmatches = max(int(round(x.real//m)) for x in obratno)
        maxmatches += nuclmatches
    return maxmatches

m = int(input())
a = input()
b = input()
ans = biba(a, b, m)
print(ans)
