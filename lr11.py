import hashlib

def generate_sha384_hash(input_text):
    # Объект хеша SHA-384
    sha384_hash = hashlib.sha384()
    
    # Кодирование введённого текста в байты и обновление объекта хэша
    sha384_hash.update(input_text.encode('utf-8'))
    
    # Получение хэша в виде шестнадцатеричной строки
    hex_dig = sha384_hash.hexdigest()
    
    return hex_dig

input_text = input("Введите текст для генерации SHA-384 хэша: ")

print(f'Введенный текст: {input_text}')

print("SHA-384 хэш введённого текста:", generate_sha384_hash(input_text))