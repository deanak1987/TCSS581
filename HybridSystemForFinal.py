import random
from hashlib import sha256
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Hash import SHA256
from Cryptodome.Util.Padding import pad, unpad

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



# Hybrid Encryption Class
class HybridEncryption:
    def __init__(self, symmetric_key_size=32):
        self.symmetric_key_size = symmetric_key_size

    # Generate a random symmetric key
    def generate_symmetric_key(self):
        return get_random_bytes(self.symmetric_key_size)

    # Encrypt plaintext using hybrid encryption
    def encrypt(self, plaintext, public_key):
        # Generate a random symmetric key
        symmetric_key = self.generate_symmetric_key()

        # Encrypt plaintext using symmetric key (AES)
        cipher = AES.new(symmetric_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        # Encrypt the symmetric key using asymmetric encryption (ElGamal or RSA)
        encrypted_key = public_key.encrypt(symmetric_key, None)

        # Return the encrypted symmetric key and the ciphertext
        return encrypted_key, cipher.iv, ciphertext

    # Decrypt ciphertext using hybrid encryption
    def decrypt(self, encrypted_key, iv, ciphertext, private_key):
        # Decrypt the symmetric key using asymmetric decryption
        symmetric_key = private_key.decrypt(encrypted_key)

        # Decrypt the ciphertext using the symmetric key (AES)
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Return the decrypted plaintext
        return decrypted_text

# Example Usage
if __name__ == '__main__':
    # Alice (Sender) Side
    # Generate Alice's public and private keys (asymmetric)
    alice_public_key, alice_private_key = generate_key_pair()

    # Generate a random plaintext to be encrypted
    plaintext = b'This is a secret message.'

    # Create an instance of the HybridEncryption class
    hybrid_encryption = HybridEncryption()

    # Encrypt the plaintext using Alice's public key
    encrypted_key, iv, ciphertext = hybrid_encryption.encrypt(plaintext, alice_public_key)

    # Send the encrypted key, IV, and ciphertext to Bob (Receiver)

    # Bob (Receiver) Side
    # Decrypt the ciphertext using Bob's private key
    decrypted_text = hybrid_encryption.decrypt(encrypted_key, iv, ciphertext, bob_private_key)

    # Print the decrypted plaintext
    print("Decrypted Plaintext:", decrypted_text.decode())
