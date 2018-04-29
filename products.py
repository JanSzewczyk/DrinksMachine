class Product:
    count = 30
    def __init__(self, name = "", prize = 0.0):
        """Inicjalizuj"""
        self.nazwa = name
        self.cena = prize
        self.ilosc = 5
        self.nr_produktu = Product.count
        Product.counting()

    def __str__(self):
        text = ""
        text += str(self.nr_produktu) + "." + self.nazwa + " :" + str(self.cena)
        return text

    @staticmethod
    def counting():
        Product.count += 1
