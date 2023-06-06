from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
pt = 'This is a top secret.'
ct = bytes.fromhex('764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2')
iv = bytes.fromhex('aabbccddeeff00998877665544332211')

f = open('words.txt')
for line in f.readlines():
    line = line.strip()
    if len(line) <= 16:
        for _ in range(16 - len(line)):
            line += '#'
        key = bytes(line, 'utf-8')
        ciph = AES.new(key, AES.MODE_CBC, iv=iv)
        ciphtex = ciph.encrypt(pad(pt.encode('utf-8'), AES.block_size))
        if ciphtex.hex() == ct.hex():
            print(line)