import hmac
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class Utils:
    @classmethod
    def generate_hmac(cls, message: str, secret_key: str) -> str:
        """生成 HMAC"""
        key = secret_key.encode()
        hmac_result = hmac.new(key, message.encode(), hashlib.sha256).digest()
        return base64.b64encode(hmac_result).decode()

    @classmethod
    def generate_hash_key(cls, key: str, length: int) -> bytes:
        """生成哈希密钥"""
        hasher = hashlib.sha256()
        hasher.update(key.encode())
        derived_key = hasher.digest()
        return derived_key[:length]  # 取前 16 字节用于 AES 密钥

    @classmethod
    def aes_encrypt(cls, message: str, key: str) -> str:
        """AES 加密"""
        hash_key = cls.generate_hash_key(key, 16)
        cipher = Cipher(algorithms.AES(hash_key), modes.ECB(), backend=default_backend())
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()

        encryptor = cipher.encryptor()
        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        return base64.b64encode(encrypted).decode()

    @classmethod
    def aes_decrypt(cls, message: str, key: str) -> str:
        """AES 解密"""
        if not message:
            return ""

        hash_key = cls.generate_hash_key(key, 16)
        cipher = Cipher(algorithms.AES(hash_key), modes.ECB(), backend=default_backend())
        encrypted_message = base64.b64decode(message)

        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_message) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted.decode()
