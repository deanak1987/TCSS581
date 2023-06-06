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


n = bytes.fromhex('DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5')
e = bytes.fromhex('010001') # (this hex value equals to decimal 65537)
C = bytes.fromhex('8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F')
d = bytes.fromhex('74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D')

print(f'Ciphertext message in hex: {hexlify(C)}')


m = exp_mod_bytes(C, d, n)
print(f'Plaintext message in hex: {hexlify(m)}')
print(f'Plaintext message in ascii: {m.decode()}')
