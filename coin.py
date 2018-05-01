class Coin:
    def __init__(self, nom=0.0, il=0):
        """Inicjalizuj"""
        self.__nominal = nom
        self.__ilosc = il

    def __str__(self):
        text = ""
        text += str(self.__nominal) + " ilość :" + str(self.__ilosc)
        return text

    def wartosc(self):
        return round(self.__nominal * self.__ilosc, 2)

    def get_nominal(self):
        """Zwróć nominał monety"""
        return round(self.__nominal, 2)

    def get_ilosc(self):
        """Zwróć ilosc monet"""
        return self.__ilosc

    def inc(self):
        """Zwieksza ilość"""
        self.__ilosc += 1

    def dec(self):
        """Zwieksza ilość"""
        self.__ilosc -= 1
