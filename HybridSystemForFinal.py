import random
from hashlib import sha256


def get_keys(h, y):
    k = sha256(bytes(h**y)).digest()
    print(len(k))
    k_E = k[:16]
    k_M = k[16:]
    return k_E, k_M


#Finds all generators of the cyclic group under modulo n
def find_generators(n):
    generators = []
    for i in range(1, n):
        if all(pow(i, j, n) != 1 for j in range(2, n)):
            generators.append(i)
    return generators
g=8
h=g**4
r=3
c1 = g**r
c = pow(c1, h**4)