from sympy import randprime, gcd
from math import prod

def generate_rsa_keys():
    # Генерируем простые числа
    p, q = randprime(100, 1000), randprime(100, 1000)
    
    while q == p:
        q = randprime(100, 1000)
    
    # Вычисляем n и функцию Эйлера от n
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Выбираем e, взаимно простое с phi
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    
    # Вычисляем d, обратное к e по модулю phi
    d = pow(e, -1, phi)
    
    # Возвращаем открытый и закрытый ключи
    return ((e, n), (d, n))

# Функция для шифрования сообщения
def encrypt_message(message, public_key):
    e, n = public_key
    # Шифруем сообщение, применяя преобразование RSA
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

# Функция для расшифровки сообщения
def decrypt_message(cipher_text, private_key):
    d, n = private_key
    # Расшифровываем сообщение, применяя преобразование RSA
    decrypted_msg = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_msg)

# Генерируем ключи
public_key, private_key = generate_rsa_keys()

# Показываем открытый ключ пользователю
print(f'Public key: {public_key}')

# Демонстрация шифрования и расшифрования
message = "RSA Test!"
encrypted_message = encrypt_message(message, public_key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = decrypt_message(encrypted_message, private_key)
print(f'Decrypted message: {decrypted_message}')
