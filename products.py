class Product:
    count = 30
    def __init__(self, name = "", prize = 0.0):
        """Inicjalizuj"""
        self.__nazwa = name
        self.__cena = prize
        self.__ilosc = 5
        self.__nr_produktu = Product.count
        Product.counting()

    def __str__(self):
        text = ""
        text += str(self.__nr_produktu) + "." + self.__nazwa + " :" + str(self.__cena)
        return text

    @staticmethod
    def counting():
        Product.count += 1

    def get_nr(self):
        """Zwraca numer produktu"""
        return self.__nr_produktu

    def get_cena(self):
        """Zwraca cenę produktu"""
        return self.__cena

    def get_ilosc(self):
        """Zwraca ilosc produktu"""
        return int(self.__ilosc)

    def dec(self):
        """Zwieksza ilość"""
        self.__ilosc -= 1