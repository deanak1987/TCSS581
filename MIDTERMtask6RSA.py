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


M = bytes.fromhex('3b5900345f6071e5aa59c23418edeaaf6d11c3c0d8a6795f4e1137b764a416aa ')
S = bytes.fromhex('31a18e6ef842398a3a4f07d6aaab4a54c893db9e19942864670dc6e5bfedb0d1a248242ef8b51d36cc6b8431b9282ca5a9645ffd85a153492e7644e124bf51f4bb50d3fbfbf40f2a7ada41eb44a63c765a879bd389fadda609b0e232aa5073ad10d79c0ae9d4b1b0260a602b5c7709a345ccc94befbb18b604df801c91642f15161e1b2953d03d5ae640352cd71b67337842734078121c120b2a8ba000ee64f2e234ccf5d9d0b40f5ebb661d4f7ede584bf166a08f04d16a70a3293773eaf8a17197c87c7c638d696fcc4285d14dd65f3b42f259efca71e0381dd3ff180d3afe87b85d401321410b383608f67c8baad6daef2a77668b77778139f7f6e82fd64f ')
e = bytes.fromhex('010001') # (this hex value equals to decimal 65537)
n = bytes.fromhex('C14BB3654770BCDD4F58DBEC9CEDC366E51F311354AD4A66461F2C0AEC6407E52EDCDCB90A20EDDFE3C4D09E9AA97A1D8288E51156DB1E9F58C251E72C340D2ED292E156CBF1795FB3BB87CA25037B9A52416610604F571349F0E8376783DFE7D34B674C2251A6DF0E9910ED57517426E27DC7CA622E131B7F238825536FC13458008B84FFF8BEA75849227B96ADA2889B15BCA07CDFE951A8D5B0ED37E236B4824B62B5499AECC767D6E33EF5E3D6125E44F1BF71427D58840380B18101FAF9CA32BBB48E278727C52B74D4A8D697DEC364F9CACE53A256BC78178E490329AEFB494FA415B9CEF25C19576D6B79A72BA2272013B5D03D40D321300793EA99F5')
print(f'Plaintext message in hex: {hexlify(M)}')

print(f'Message signature in hex: {hexlify(S)}')

m = exp_mod_bytes(S, e, n)
print(f'Verify Signature in hex: {hexlify(m)}')
print(f'Verified? {M in m}!')


