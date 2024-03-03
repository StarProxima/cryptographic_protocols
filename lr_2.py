def gcd_extended(a, b):
    """Расширенный алгоритм Евклида."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def euler_phi(m):
    """Вычисляет значение функции Эйлера."""
    result = 1
    for i in range(2, m):
        if gcd_extended(i, m)[0] == 1:
            result += 1
    return result

class ModularExponentiation:
    def __init__(self, modulus):
        self.modulus = modulus

    def add_mod(self, a, b):
        """Сложение по модулю."""
        return (a + b) % self.modulus

    def mul_mod(self, a, b):
        """Умножение по модулю."""
        return (a * b) % self.modulus

    def inv_mod(self, a):
        """Нахождение обратного элемента по модулю."""
        gcd, x, _ = gcd_extended(a, self.modulus)
        if gcd != 1:
            raise ValueError("Обратный элемент не существует.")
        return x % self.modulus

    def pow_mod(self, base, exponent):
        """Вычисление степени по модулю."""
        if exponent == 0:
            return 1
        elif exponent > 0:
            # Малая теорема Ферма для положительных степеней
            result = 1
            for _ in range(exponent):
                result = self.mul_mod(result, base)
            return result
        else:
            # Теорема Эйлера для отрицательных степеней
            phi = euler_phi(self.modulus)
            inv_base = self.inv_mod(base)
            positive_exponent = (-exponent) % phi
            result = 1
            for _ in range(positive_exponent):
                result = self.mul_mod(result, inv_base)
            return result

# Пример использования
mod_exp = ModularExponentiation(17)
print(mod_exp.pow_mod(3, 5))  # 3^5 mod 17
print(mod_exp.pow_mod(3, -5))  # 3^(-5) mod 17, используя обратный элемент и теорему Эйлера
