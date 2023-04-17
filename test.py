x = b'x00x00x00x00'
y = int.from_bytes(x, byteorder='big')
z = ((y << 16) | (y >> 16)) & 0xffffffff
print(z.to_bytes(4, byteorder='big'))
