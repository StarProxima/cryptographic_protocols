def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def euler_phi(m):
    factors = prime_factors(m)
    result = m
    for factor in factors:
        result *= (1 - 1 / factor)
    return int(result)

def gcd_extended(a, b):
    if a == 0:
        print(f"Текущие значения: gcd={b}, x=0, y=1, a={a}, b={b}")
        return b, 0, 1
    else:
        gcd, x1, y1 = gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        print(f"Текущие значения: gcd={gcd}, x={x}, y={y}, a={a}, b={b}")
        return gcd, x, y

def modular_linear_equation_solver(a, b, m):
    """Решение сравнения ax ≡ b (mod m)"""
    g, x, y = gcd_extended(a, m)
    solutions = []
    if b % g == 0:
        if g == 1:  # a и m взаимно просты, можно применить функцию Эйлера
            phi_m = euler_phi(m)
            print(f"Функция Эйлера (phi) для m = {m} равна {phi_m}")
            inv_a = pow(a, phi_m - 1, m)
            x0 = (inv_a * b) % m
            print(f"Обратный элемент a по модулю m с использованием функции Эйлера: {inv_a}")
            solutions.append(x0)
        else:  # Используем расширенный алгоритм Евклида для решения
            x0 = (x * (b // g)) % m
            for i in range(g):
                solution = (x0 + i * (m // g)) % m
                print(f"Решение: x = {solution} (для i = {i})")
                solutions.append(solution)
        return solutions
    else:
        print("Сравнение не имеет решений.")
        return None

# Пример использования функции с логированием
a, b, m = 3, 19, 34  # Пример значений
solutions = modular_linear_equation_solver(a, b, m)
print(f"Все решения: {solutions}")
