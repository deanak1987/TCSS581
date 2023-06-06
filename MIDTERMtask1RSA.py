from binascii import hexlify


def mult_bytes(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    length = len(b1) + len(b2)
    sol = b1i * b2i
    return sol.to_bytes(length, 'big')


def exp_mod_bytes(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    length = len(b1) * len(b2)
    sol = b1i ** b2i
    return sol.to_bytes(length, 'big')


def mult_mod_bytes(b1, b2, b3):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    b3i = int.from_bytes(b3, 'big')
    sol = (b1i * b2i) % b3i
    length = len(b3)
    return sol.to_bytes(length, 'big')


def mod_inv_bytes(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    length = len(b2)
    return pow(b1i, -1, b2i).to_bytes(length, 'big')


def phi(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    sol = (b1i - 1) * (b2i - 1)
    length = len(b1) + len(b2)
    return sol.to_bytes(length, 'big')


p = bytes.fromhex('F7E75FDC469067FFDC4E847C51F452DF')
q = bytes.fromhex('E85CED54AF57E53E092113E62F436F4F')
e = bytes.fromhex('0D88C3')

d = mod_inv_bytes(e, phi(p, q))
print(f'Private key, d = {hexlify(d)}')
