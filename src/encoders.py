import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Base64 encoding
def encode_base64(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

# MD5 hashing
def hash_md5(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

# SHA-256 hashing
def hash_sha256(text):
    sha_hash = hashlib.sha256()
    sha_hash.update(text.encode('utf-8'))
    return sha_hash.hexdigest()

# AES encryption
def encrypt_aes(text, key):
    if not key or len(key) not in [16, 24, 32]:
        return "Invalid key length. Key must be 16, 24, or 32 bytes long."

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key.encode('utf-8')), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Padding to ensure text is a multiple of block size
    pad = 16 - (len(text) % 16)
    padded_text = text + pad * chr(pad)

    ciphertext = encryptor.update(padded_text.encode('utf-8')) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode('utf-8')
