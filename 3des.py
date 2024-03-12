from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad_data(data):
    # Calculate the number of bytes needed to pad the data
    pad_len = 8 - (len(data) % 8)
    # Pad the data with the required number of bytes
    padded_data = data + bytes([pad_len] * pad_len)
    return padded_data

def encrypt(data, key):
    padded_data = pad_data(data)
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    # Remove padding from decrypted data
    pad_len = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad_len]
    return decrypted_data

def main():
    # Input data and key
    data = b"Hello, this is a message to encrypt using Triple DES!"
    key = get_random_bytes(24)  # Generate a random 24-byte key (Triple DES key size)

    # Encrypt the data
    ciphertext = encrypt(data, key)
    print("Encrypted:", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_data = decrypt(ciphertext, key)
    print("Decrypted:", decrypted_data.decode())

if __name__ == "__main__":
    main()
