from Dis import Dis


class Roots(Dis):
    def __init__(self, a, b, c, value):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.value = float(value)

    def roots_count(self):
        if self.value > 0:
            x1 = (-self.b + self.value**1/2) / (2 * self.a)
            x2 = (-self.b - self.value**1/2) / (2 * self.a)
            return float(x1), float(x2)
        elif self.value == 0:
            x1 = -self.b / (2 * self.a)
            return float(x1)
        else:
            return "Нет корней"
