# Dean Kelley
# 4/17/2023
# TCSS 581 Chacha20 Assignment

import time
from binascii import hexlify


# Integer addition of two bytes modulo 32
def badd(b1, b2):
    b1_int = int.from_bytes(b1, byteorder='big')
    b2_int = int.from_bytes(b2, byteorder='big')
    ba = (b1_int + b2_int) % 2 ** 32
    return ba.to_bytes(4, byteorder='big')


# XOR of two bytes
def bxor(b1, b2): # use xor for bytes
    return bytes(a1 ^ a2 for a1, a2 in zip(b1, b2))


# Rotation by b bits
def rot(x, b):
    xint = int.from_bytes(x, byteorder='big')
    shift_int = ((xint << b) | (xint >> 32 - b)) & 0xffffffff
    byte_rotated = shift_int.to_bytes(4, byteorder='big')
    return byte_rotated


# QuarterRound
def qr(b1, b2, b3, b4):
    b1 = badd(b1, b2)
    b4 = rot(bxor(b4, b1), 16)
    b3 = badd(b3, b4)
    b2 = rot(bxor(b2, b3), 12)
    b1 = badd(b1, b2)
    b4 = rot(bxor(b4, b1), 8)
    b3 = badd(b3, b4)
    b2 = rot(bxor(b2, b3), 7)
    return b1, b2, b3, b4


# Performs column and diagonal quartrounds to block
def inner_block(array):
    array[0], array[4], array[8], array[12] = qr(array[0], array[4], array[8], array[12])
    array[1], array[5], array[9], array[13] = qr(array[1], array[5], array[9], array[13])
    array[2], array[6], array[10], array[14] = qr(array[2], array[6], array[10], array[14])
    array[3], array[7], array[11], array[15] = qr(array[3], array[7], array[11], array[15])
    array[0], array[5], array[10], array[15] = qr(array[0], array[5], array[10], array[15])
    array[1], array[6], array[11], array[12] = qr(array[1], array[6], array[11], array[12])
    array[2], array[7], array[8], array[13] = qr(array[2], array[7], array[8], array[13])
    array[3], array[4], array[9], array[14] = qr(array[3], array[4], array[9], array[14])
    return array


# Creates and processes the serialized block
def chacha20_block(key, counter, nonce):
    c = bytes.fromhex('617078653320646e79622d326b206574')
    state = []
    for i in range(0, 16, 4):
        state.append(c[i:i+4])
    for i in range(0, 32, 4):
        temp = key[i:i+4]
        state.append(temp[::-1])
    state.append(counter)
    for i in range(0, 12, 4):
        temp = nonce[i:i+4]
        state.append(temp[::-1])
    working_state = []
    for i in range(len(state)):
        working_state.append(state[i])
    for i in range(10):
        working_state = inner_block(working_state)
    block = []
    for i in range(len(state)):
        block.append(badd(state[i], working_state[i]))
    serialized_block = b''
    for i in range(len(state)):
        serialized_block += (block[i][::-1])
    return serialized_block


# Ceiling division
def ceildiv(a, b):
    return -(a // -b)


# Chacha20 encryption/decryption algorithm
def chacha20_encrypt(key, counter, nonce, plaintext):
    encrypted_message = b''
    time_nm = []
    key_stream = b''
    for i in range((ceildiv(len(plaintext), 64))):
        tic = time.time_ns()
        key_stream = chacha20_block(key, badd(counter, i.to_bytes(4, byteorder='big')), nonce)
        toc = time.time_ns()
        time_nm.append(toc - tic)
        print('Key Stream round ' + str(i+1) + ': ' + str(hexlify(key_stream)))
        block = plaintext[i * 64: i * 64 + 64]
        print('Block round ' + str(i+1) + ': ' + str(hexlify(block)))
        enc = bxor(block, key_stream)
        encrypted_message += enc
    print('Bits per second = ' + str(round(len(key_stream) * 8 / (sum(time_nm) / len(time_nm)) * 10**9)))
    return encrypted_message


Key = bytes.fromhex('00:01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f:10:11:12:13:14:'
                    '15:16:17:18:19:1a:1b:1c:1d:1e:1f'.replace(':', ' '))
Counter = bytes.fromhex('00000001')
Nonce = bytes.fromhex('00:00:00:00:00:00:00:4a:00:00:00:00'.replace(':', ' '))
Plaintext = bytes.fromhex('4c 61 64 69 65 73 20 61 6e 64 20 47 65 6e 74 6c'
                          '65 6d 65 6e 20 6f 66 20 74 68 65 20 63 6c 61 73'
                          '73 20 6f 66 20 27 39 39 3a 20 49 66 20 49 20 63'
                          '6f 75 6c 64 20 6f 66 66 65 72 20 79 6f 75 20 6f'
                          '6e 6c 79 20 6f 6e 65 20 74 69 70 20 66 6f 72 20'
                          '74 68 65 20 66 75 74 75 72 65 2c 20 73 75 6e 73'
                          '63 72 65 65 6e 20 77 6f 75 6c 64 20 62 65 20 69'
                          '74 2e')

Ciphertext = chacha20_encrypt(Key, Counter, Nonce, Plaintext)

print()
print('Plaintext: ', Plaintext)
print('Plaintext Hex: ', hexlify(Plaintext))
print('Ciphertex Hex: ', hexlify(Ciphertext))


