class Dis:

    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.value = 0

    def discriminant_count(self):
        self.value = self.b**2 - 4 * self.a * self.c
        return float(self.value)
