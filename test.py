from binascii import hexlify


def exp_mod_bytes(b1, b2, b3):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    b3i = int.from_bytes(b3, 'big')
    length = len(b3)
    sol = pow(b1i, b2i, b3i)
    return sol.to_bytes(length, 'big')


def mod_inv_bytes(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    length = len(b2)
    return pow(b1i, -1, b2i).to_bytes(length, 'big')


def mult_bytes(b1, b2):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    length = len(b1) + len(b2)
    sol = b1i * b2i
    return sol.to_bytes(length, 'big')


def mult_mod_bytes(b1, b2, b3):
    b1i = int.from_bytes(b1, 'big')
    b2i = int.from_bytes(b2, 'big')
    b3i = int.from_bytes(b3, 'big')
    sol = (b1i * b2i) % b3i
    length = len(b3)
    return sol.to_bytes(length, 'big')


M1 = 10
M2 = 9
M1 =M1.to_bytes(4, 'big')
n = bytes.fromhex('DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5')
e = bytes.fromhex('010001') # (this hex value equals to decimal 65537)
d = bytes.fromhex('74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D')
print(f'Plaintext message1 in hex: {hexlify(M1)}')

C1 = exp_mod_bytes(M1, e, n)
print(f'Ciphertext message1 in hex: {hexlify(C1)}')
#
C2 = (int.from_bytes(C1,'big') * pow(9/10, int.from_bytes(e, 'big'))) % int.from_bytes(n, 'big')

m = exp_mod_bytes(C1, d, n)
print(f'Verify Plaintext in hex: {hexlify(m)}')
print(f'Verified? {M1 in m}!')

m2 = exp_mod_bytes(C2, d, n)
print(f'Verify Plaintext in hex: {hexlify(m2)}')
print(f'Verified? {M2 in m2}!')

