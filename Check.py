class Check:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def check_values(self):
        try:
            if ((type(float(self.__a)) and type(float(self.__b)) and
               type(float(self.__c))) is float) and self.__a != 0:
                return True
        except ValueError:
            return False
