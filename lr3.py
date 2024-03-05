class Polynom:
    def __init__(self, body):
        self.body = body

    def degree(self):
        return len(self.body) - 1

    @staticmethod
    def by_degree(degree):
        return Polynom([0] * degree + [1])

    @staticmethod
    def by_number(number):
        return Polynom([int(x) for x in bin(number)[2:]])

    def print(self):
        terms = []
        for i, coeff in enumerate(self.body[::-1]):
            if coeff:
                if i == 0:
                    terms.append('1')
                else:
                    terms.append(f'x^{i}')
        print(' + '.join(terms[::-1]))

    def __add__(self, other):
        max_degree = max(self.degree(), other.degree())
        new_poly = [((self.body[i] if i <= self.degree() else 0) ^
                     (other.body[i] if i <= other.degree() else 0)) for i in range(max_degree + 1)]
        return Polynom(new_poly)

    def __mul__(self, other):
        new_degree = self.degree() + other.degree()
        new_poly = [0] * (new_degree + 1)
        for i in range(self.degree() + 1):
            if not self.body[i]:
                continue
            for j in range(other.degree() + 1):
                new_poly[i + j] ^= self.body[i] * other.body[j]
        return Polynom(new_poly)

    def __ge__(self, other):
        if self.degree() != other.degree():
            return self.degree() >= other.degree()
        for i in range(self.degree(), -1, -1):
            if self.body[i] != other.body[i]:
                return self.body[i] > other.body[i]
        return True

    def __truediv__(self, other):
        divided_poly = Polynom(self.body)
        while divided_poly.degree() >= other.degree():
            division_part_degree = divided_poly.degree() - other.degree()
            division_part_poly = Polynom.by_degree(division_part_degree)
            sub_part_poly = other * division_part_poly
            divided_poly += sub_part_poly
        if divided_poly.degree() == other.degree() and divided_poly >= other:
            divided_poly += other
        return Polynom(divided_poly.body)


def polynom_is_irreducible(poly):
    max_search_degree = poly.degree() // 2
    max_search_number = 2**(max_search_degree + 1) - 1
    for i in range(2, max_search_number + 1):
        check_poly = Polynom.by_number(i)
        remainder = poly / check_poly
        if remainder.degree() == -1:
            return False
    return True


def polynom_is_primitive_in_gp(poly, gp_degree):
    if polynom_is_irreducible(poly):
        max_degree = 2**gp_degree - 1
        for i in range(1, max_degree + 1):
            poly_number = 2**i
            check_poly = Polynom.by_number(poly_number + 1)
            remainder = check_poly / poly
            if remainder.degree() == -1:
                return False
        return True
    return False


# Пример использования
poly_true = Polynom.by_number(32 + 4 + 1)
print(polynom_is_irreducible(poly_true))

# poly_false = Polynom.by_number(128 + 1)
# print(polynom_is_irreducible(poly_false))
# print(polynom_is_primitive_in_gp(poly_true, 5))
