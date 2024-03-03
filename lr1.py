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
    
def euler_method(a, b, m):
    g, _, _ = gcd_extended(a, m)

    if b % g != 0 and g != 1:
        print("Сравнение не может быть решено.")
        return None

    phi_m = euler_phi(m)
    print(f"Функция Эйлера (phi) для m = {m} равна {phi_m}")
    inv_a = pow(a, phi_m - 1, m)
    x0 = (inv_a * b) % m
    print(f"Обратный элемент a по модулю m с использованием функции Эйлера: {inv_a}")
    return x0

def gcd_extended_method(a, b, m):
    g, x, y = gcd_extended(a, m)
    solutions = []

    if b % g != 0:
        print("Сравнение не может быть решено.")
        return None

    x0 = (x * (b // g)) % m
    for i in range(g):
        solution = (x0 + i * (m // g)) % m
        print(f"Решение: x = {solution} (для i = {i})")
        solutions.append(solution)
    return solutions

def modular_linear_equation_solver(a, b, m):
    """Решение сравнения ax ≡ b (mod m)"""
    
    print(f"Функция Эйлера: {euler_method(a, b, m)}")
    print(f"Расширенный алгоритма Евклида: {gcd_extended_method(a, b, m)}")
    

modular_linear_equation_solver(3, 19, 34)
