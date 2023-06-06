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
M = b'I owe you $2000.'
d = bytes.fromhex('74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D')

print(f'Plaintext message in hex: {hexlify(M)}')

sig = exp_mod_bytes(M, d, n)
print(f'Message signature in hex: {hexlify(sig)}')

m = exp_mod_bytes(sig, e, n)
print(f'Verify Signature in hex: {hexlify(m)}')
print(f'Verified? {M in m}!')

M_alt = b'I owe you $3000.'
sig = exp_mod_bytes(M_alt, d, n)
print(f'Message signature in hex: {hexlify(sig)}')

m = exp_mod_bytes(sig, e, n)
print(f'Verify Signature in hex: {hexlify(m)}')
print(f'Verified? {M in m}!')
