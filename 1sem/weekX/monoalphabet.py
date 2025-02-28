import random

class Monoalphabet:
    alphabet = ""  # TODO

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        pass  # TODO


key = Monoalphabet.alphabet[:]
random.shuffle(key)
cipher = Monoalphabet(key)
line = input()
while line:
    print(cipher.encode(line))
    line = input()