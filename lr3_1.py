def add_polynomials(a, b):
    # Сложение многочленов в GF(2) - это просто XOR их коэффициентов
    return [x ^ y for x, y in zip(a, b)]

def multiply_polynomials(a, b):
    # Инициализация результата
    result = [0] * (len(a) + len(b) - 1)
    # Умножение каждого коэффициента из первого многочлена
    # на каждый коэффициент из второго многочлена
    for i, coeff_a in enumerate(a):
        for j, coeff_b in enumerate(b):
            result[i + j] ^= coeff_a & coeff_b
            # Выводим шаг умножения
            print(f"Шаг умножения: {result}")
    # Возвращаем результат без ведущих нулей
    return [coeff for coeff in result if coeff != 0]

def divide_polynomials(dividend, divisor):
    # Копия делимого, поскольку мы будем изменять его в процессе деления
    remainder = list(dividend)
    # Результат деления
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    # Главный цикл деления
    for i in range(len(dividend) - len(divisor), -1, -1):
        # Если старший коэффициент делимого не ноль, то выполняем деление
        if remainder[i + len(divisor) - 1]:
            quotient[i] = 1  # Установка соответствующего коэффициента частного
            # Вычитание (XOR) divisor из делимого
            for j in range(len(divisor)):
                remainder[i + j] ^= divisor[j]
            print(f"Шаг деления: {remainder}")
    # Удаление ведущих нулей в остатке
    remainder = [coeff for coeff in remainder if coeff != 0]
    return quotient, remainder


def task1():
    # Примеры из задачи
    examples = [
        ([1, 0, 1, 1], [1, 1]),  # F(x) = x^3 + x + 1, G(x) = x + 1
        ([1, 0, 1], [1, 1]),     # F(x) = x^2 + 1, G(x) = x + 1
        ([1, 0, 1, 0, 1], [1, 0, 1]),  # F(x) = x^3 + x^2 + 1, G(x) = x^2 + 1
        ([1, 0, 0, 1, 1], [1, 0, 1]),  # F(x) = x^4 + x^2 + 1, G(x) = x^2 + x + 1
        ([1, 0, 0, 1, 1], [1, 1]),     # F(x) = x^4 + x^2 + x + 1, G(x) = x + 1
        ([1, 0, 1, 1, 0, 1], [1, 1, 1]),
    ]

    # Выполнение операций для каждого примера
    for i, (f, g) in enumerate(examples, start=1):
        print(f"Пример {i}.")

        # Сложение
        print("Сложение многочленов:")
        sum_result = add_polynomials(f, g)
        print(f"Сумма: {sum_result}\n")
 
        # Умножение
        print("Умножение многочленов:")
        mult_result = multiply_polynomials(f, g)
        print(f"Произведение: {mult_result}\n")

        # Деление
        print("Деление многочленов:")
        quotient, remainder = divide_polynomials(f, g)
        print(f"Частное: {quotient}, Остаток: {remainder}\n")

        # Разделитель между примерами
        print("-" * 50)