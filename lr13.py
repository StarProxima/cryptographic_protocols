from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_ctr_encrypt(plaintext, key):
    # Генерируем случайный инициализирующий вектор (IV)
    iv = os.urandom(16)
    print(f"IV: {iv}")
    # Создаем объект шифра
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Шифруем данные
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    # Возвращаем инициализирующий вектор и шифртекст
    return (iv, ciphertext)

def aes_ctr_decrypt(iv, ciphertext, key):
    # Создаем объект шифра с тем же ключом и IV
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Расшифровываем данные
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# Пример использования
key = os.urandom(32)  # AES-256 требует ключ длиной 32 байта
print(f'Ключ: {key}')
plaintext = b"AES Test"
print(f'Текст: {plaintext}')

iv, ciphertext = aes_ctr_encrypt(plaintext, key)
print("Зашифрованный текст:", ciphertext)

decrypted_text = aes_ctr_decrypt(iv, ciphertext, key)
print("Расшифрованный текст:", decrypted_text)