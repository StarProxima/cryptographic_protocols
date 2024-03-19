from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii


# Генерация пары ключей RSA
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Подпись сообщения с использованием приватного ключа
def sign_message(private_key, message):
    rsakey = RSA.import_key(private_key)
    msg_hash = SHA256.new(message.encode())
    signer = pkcs1_15.new(rsakey)
    signature = signer.sign(msg_hash)
    return binascii.hexlify(signature).decode()

# Проверка подписи сообщения с использованием публичного ключа
def verify_signature(public_key, message, signature):
    rsakey = RSA.import_key(public_key)
    msg_hash = SHA256.new(message.encode())
    signature = binascii.unhexlify(signature)
    try:
        pkcs1_15.new(rsakey).verify(msg_hash, signature)
        return True
    except (ValueError, TypeError):
        return False

# Пример использования
private_key, public_key = generate_keys()

print(f'Закрытый ключ: {private_key}')
print(f'Открытый ключ: {public_key}')

# Подпись сообщения
message = "Hello, World!"
print(f'Сообщение: {message}')
signature = sign_message(private_key, message)
print(f"Подпись: {signature}")

# Проверка подписи
verification_result = verify_signature(public_key, message, signature)
print(f"Результат проверки подписи: {'Успешно' if verification_result else 'Ошибка'}")