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


M = b'Launch a missile.'
S = bytes.fromhex('643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F')
e = bytes.fromhex('010001') # (this hex value equals to decimal 65537)
n = bytes.fromhex('AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115')
print(f'Plaintext message in hex: {hexlify(M)}')

print(f'Message signature in hex: {hexlify(S)}')

m = exp_mod_bytes(S, e, n)
print(f'Verify Signature in hex: {hexlify(m)}')
print(f'Verified? {M in m}!')
