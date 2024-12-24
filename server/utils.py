def log_activity(activity):
    """Log server-side activity."""
    with open("server_logs.txt", "a") as log_file:
        log_file.write(activity + "\n")

from Crypto.Cipher import AES
import base64
import hashlib

def decrypt_data(data, key):
    """Decrypt data using a symmetric key."""
    key = hashlib.sha256(key.encode()).digest()
    data = base64.b64decode(data)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()
