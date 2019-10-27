class Discriminant:

    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__discriminant_value = 0

    def get_discriminant(self):
        self.__discriminant_value = self.__b ** 2 - 4 * self.__a * self.__c
        return self.__discriminant_value


class Roots:
    def __init__(self, a, b, discriminant_value):
        self.__a = float(a)
        self.__b = float(b)
        self.__discriminant_value = discriminant_value

    def get_roots(self):
        if self.__discriminant_value > 0:
            x1 = (-self.__b + self.__discriminant_value ** (1 / 2)) / (2 * self.__a)
            x2 = (-self.__b - self.__discriminant_value ** (1 / 2)) / (2 * self.__a)
            return [x1, x2]
        elif self.__discriminant_value == 0:
            x1 = -self.__b / (2 * self.__a)
            return x1
        else:
            return "Нет корней"
