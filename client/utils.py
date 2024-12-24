from Crypto.Cipher import AES
import base64
import hashlib

def encrypt_data(data, key):
    """Encrypt data using a symmetric key."""
    key = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_data(data, key):
    """Decrypt data using a symmetric key."""
    key = hashlib.sha256(key.encode()).digest()
    data = base64.b64decode(data)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()
