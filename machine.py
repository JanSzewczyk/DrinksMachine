from tkinter import *
from throwing_coins import *
from products import *
from give_back_coins import *
import time

class Maschine(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        self.drinks = []                            #lista obiektów napoi
        self.sum_coins = 0.0                        #suma wrzuconych monet
        self.text = ""                              #tekst na screenie
        self.monety_wrzucane = []                   #lista wrzuconych monet
        super(Maschine, self).__init__(master)
        self.grid()
        self.inicjalize_drinks()
        self.create_widgets()

    def create_widgets(self):
        """Tworzy widgety naszej maszyny"""
        # Lista produktów
        self.products = Text(self, width=25, height=22, font=("Courier",13,"bold"), wrap=WORD)
        self.products.grid(row=0, column=0, columnspan=2, rowspan=35, sticky=W)
        self.write_products()

        # Wrzuć monetę
        self.key1 = Button(self, text="Wrzuć monete", command=self.throw_coins)
        self.key1.grid(row=2, column=2, columnspan=3, sticky=W)

        # Wyświetlacz
        self.screen = Text(self, width=13, height=9, wrap=WORD)
        self.screen.grid(row=4, column=3, columnspan=6, rowspan=4, sticky=W)
        self.screen.insert(0.0,  "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)

        # Keypad
        self.key1 = Button(self, text="  1  ", command=lambda: self.keys_operation(1))
        self.key1.grid(row=10, column=3, sticky=W)

        self.key2 = Button(self, text="  2  ", command=lambda: self.keys_operation(2))
        self.key2.grid(row=10, column=4, sticky=W)

        self.key3 = Button(self, text="  3  ", command=lambda: self.keys_operation(3))
        self.key3.grid(row=10, column=5, sticky=W)

        self.key4 = Button(self, text="  4  ", command=lambda: self.keys_operation(4))
        self.key4.grid(row=11, column=3, sticky=W)

        self.key5 = Button(self, text="  5  ", command=lambda: self.keys_operation(5))
        self.key5.grid(row=11, column=4, sticky=W)

        self.key6 = Button(self, text="  6  ", command=lambda: self.keys_operation(6))
        self.key6.grid(row=11, column=5, sticky=W)

        self.key7 = Button(self, text="  7  ", command=lambda: self.keys_operation(7))
        self.key7.grid(row=12, column=3, sticky=W)

        self.key8 = Button(self, text="  8  ", command=lambda: self.keys_operation(8))
        self.key8.grid(row=12, column=4, sticky=W)

        self.key9 = Button(self, text="  9  ", command=lambda: self.keys_operation(9))
        self.key9.grid(row=12, column=5, sticky=W)

        self.key_del = Button(self, text="del ", command=lambda: self.keys_operation(10))
        self.key_del.grid(row=13, column=3, sticky=W)

        self.key0 = Button(self, text="  0  ", command=lambda: self.keys_operation(0))
        self.key0.grid(row=13, column=4, sticky=W)

        self.key_ok = Button(self, text=" OK", command=lambda: self.keys_operation(11))
        self.key_ok.grid(row=13, column=5, sticky=W)

        # Zwróć monety
        self.key_oddaj = Button(self, text="Oddaj monety", command=lambda: self.g_b_coins())
        self.key_oddaj.grid(row=20, column=2, columnspan=3, sticky=W)

    def inicjalize_drinks(self):
        """Tworzenie napoi"""
        nazwy = ["Coca-Cola", "Coca-Cola Light", "Coca-Cola Zero", "Pepsi", "Pepsi Light", "Pepsi Wild Cherry", "Sprite",
                 "Fanta", "7 Up", "Mirinda", "Mountain Dew", "Lipton", "Nestea", "Monster",
                 "Tiger", "Black", "RedBull", "OSHEE", "Kropla Beskidu", "Żywiec Zdrój", "Muszynianka"]
        cena = [2.5, 2.8, 2.65, 3.0, 3.2, 2.9, 3.5,
                3.0, 2.7, 3.25, 3.5, 2.0, 2.35, 5.5,
                3.0, 2.5, 7.5, 3.5, 1.5, 1.6, 1.29]

        self.drinks = [Product(name=nazwy[x], prize=cena[x]) for x in range(21)]

    def write_products(self):
        """Wypełnienie listy produktów"""
        lista = ""
        for i in self.drinks:
            lista += str(i) + "\n"

        self.products.insert(0.0, lista)

    def throw_coins(self):
        """Mechanizm wrzucania monet"""
        pocket = Tk()
        pocket.title("Portfel")
        pckt = Throwing_coins(pocket)
        pocket.mainloop()

        moneta = pckt.get_coin()
        if moneta != 0.0:
            self.sum_coins += moneta
            self.sum_coins = round(self.sum_coins, 2)
            self.monety_wrzucane.append(moneta)
            print(self.monety_wrzucane)
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)

    def g_b_coins(self):
        """mechanizm wyrzucania monet"""
        mach = Tk()
        mach.title("Pieniądze zwrócone XD")
        gbc = Give_Back_coins(mach)
        mach.mainloop()

    def keys_operation(self, key):
        """Operacje na przyciskach 0,1,2,..."""
        #usunięcie numerka
        if key == 10:
            self.text = ""
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)
        #akceptowanie produktu
        elif (key == 11) and not(self.text == ""):
            change = int(self.text)
            if (change >= 30) and (change <= 50):
                #kupowanie napoi
                pass
            else:
                self.screen.delete(0.0, END)
                self.screen.insert(0.0, "Brak produktu !!\nWybierz ponownie ")
                self.text = ""
        #dodawanie cyfr
        elif (0 <= key) and (key <= 9):
            self.text += str(key)
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)
