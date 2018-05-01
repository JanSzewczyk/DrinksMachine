from tkinter import *
from throwing_coins import *
from products import *
from give_back_coins import *
from coin import *
import time

class Maschine(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        self.drinks = []                            #lista obiektów napoi
        self.sum_coins = 0.0                        #suma wrzuconych monet
        self.text = ""                              #tekst na screenie
        self.monety_wrzucane = []                   #lista wrzuconych monet
        self.reszta = 0.0                           #reszta
        self.monety_w_automacie = []                #lista obiektow monet
        self.suma_w_automacie = 0.0                 #suma monet znajdujących się w automacie
        self.reszta_coin = []                       #lista monet ktore zraca
        self.kupione_produkty = []

        super(Maschine, self).__init__(master)
        self.grid()
        self.inicjalize_drinks()
        self.inicjalize_coins()
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

        # Weź resztę
        self.key_reszta = Button(self, text="Weź resztę", command=lambda: self.take_coins())
        self.key_reszta.grid(row=23, column=2, columnspan=3, sticky=W)

        #odbierz produkt
        self.wez = Button(self, text="               Weź              ", font=("Courier", 15, "bold"),
                           background="red")
        self.wez.grid(row=37, column=0, columnspan=7, sticky=W)

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

    def inicjalize_coins(self):
        """Tworzenie monet"""
        nominal = [5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
        ilosc = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.monety_w_automacie = [Coin(nom=nominal[x], il=ilosc[x]) for x in range(9)]

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
        self.monety_reszta = self.monety_wrzucane
        self.monety_wrzucane = []
        self.sum_coins = 0.0
        self.text = ""
        self.screen.delete(0.0, END)
        self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)
        #test
        print("Monety zwrócone :", self.monety_reszta)
        print("Monety wrzucone :", self.monety_wrzucane)

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
                for i in self.drinks:
                    if change == i.get_nr():
                        obj = i

                #porównanie ceny i monet w automacie
                if obj.get_ilosc() == 0:
                    self.screen.delete(0.0, END)
                    self.screen.insert(0.0, "Brak towaru !!\nWybierz ponownie ")
                    self.text = ""

                elif self.sum_coins > obj.get_cena():
                    self.reszta = self.sum_coins - obj.get_cena()
                    print("Reszta :", self.reszta)
                    self.rest(obj)

                elif self.sum_coins == obj.get_cena():
                    self.reszta = 0.0
                    self.sum_coins = 0.0

                    # dodawanie wrzuconych monet do monet w maszynie
                    for j in self.monety_wrzucane:
                        for k in self.monety_w_automacie:
                            if j == k.get_nominal():
                                k.inc()

                    self.kupione_produkty.append(obj.get_nazwa())
                    obj.dec()
                    print(self.kupione_produkty)
                    self.monety_wrzucane = []
                    self.text = ""
                    self.screen.delete(0.0, END)
                    self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text + "\nWeź produkt ")
                else:
                    self.screen.delete(0.0, END)
                    self.screen.insert(0.0, "Za mało pieniędzy !!\nWybierz ponownie ")
                    self.text = ""
            else:
                self.screen.delete(0.0, END)
                self.screen.insert(0.0, "Nie właściwy numer !!\nWybierz ponownie ")
                self.text = ""
        #dodawanie cyfr
        elif (0 <= key) and (key <= 9):
            self.text += str(key)
            self.screen.delete(0.0, END)
            self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)

    def rest(self, drink):
        # dodawanie wrzuconych monet do monet w maszynie
        for j in self.monety_wrzucane:
            for k in self.monety_w_automacie:
                if j == k.get_nominal():
                    k.inc()

        # oblicanie sumy w automacie
        for i in self.monety_w_automacie:
            self.suma_w_automacie += i.wartosc()
        self.suma_w_automacie = round(self.suma_w_automacie, 2)

        print(self.suma_w_automacie)

        for obj in self.monety_w_automacie:
            print(obj)

        if self.reszta < self.suma_w_automacie:
            # obliczanie reszty
            for l in self.monety_w_automacie:
                logic = True
                while logic:
                    if (round(self.reszta, 2) - l.get_nominal() >= 0) and (l.get_ilosc() > 0):
                        self.reszta_coin.append(l.get_nominal())
                        self.reszta -= l.get_nominal()
                        self.reszta = round(self.reszta, 2)
                        l.dec()
                    else:
                        logic = False
                if self.reszta == 0.0:
                    break

            if (self.reszta == 0.0) and (drink.get_ilosc() > 0):
                self.monety_wrzucone = []
                print(drink.get_nazwa())
                print(drink.get_ilosc())
                self.kupione_produkty.append(drink.get_nazwa())
                drink.dec()
                self.sum_coins = 0.0
                self.text = ""
                self.screen.delete(0.0, END)
                self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text + "\nWeź produkt ")
            else:
                lista = [x for x in self.monety_wrzucane]

                for i in self.reszta_coin:
                    lista.remove(i)

                for j in lista:
                    for k in self.monety_w_automacie:
                        if j == k.get_nominal():
                            k.dec()

                print("reszta :", self.reszta_coin)
                print("\nlista :", lista)
                self.reszta_coin = self.monety_wrzucane
                self.monety_wrzucane = []
                lista = []
                self.sum_coins = 0.0
                self.text = ""
                self.screen.delete(0.0, END)
                self.screen.insert(0.0, "Wrzuć odliczoną kwotę!! \nWybierz ponownie ")

        print("\n\n Monety oddane: ", self.reszta_coin, "\n\n")
        for obj in self.monety_w_automacie:
            print(obj)
        print(self.kupione_produkty)

    def take_coins(self):
        mach = Tk()
        mach.title("WEŹ RESZTĘ !!!")
        gbc = Give_Back(mach, self.reszta_coin)
        mach.mainloop()
        self.reszta_coin = []
        self.text = ""
        self.screen.delete(0.0, END)
        self.screen.insert(0.0, "Kwota :" + str(self.sum_coins) + "\nNumer :" + self.text)
        #test
        print("Monety zwrócone :", self.reszta_coin)
        print("Monety wrzucone :", self.monety_wrzucane)