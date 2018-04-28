from tkinter import *

class Throwing_coins(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        self.coins = 0.0
        super(Throwing_coins, self).__init__(master)
        self.grid()
        self.create_widgets(master)

    def create_widgets(self,X):
        """Tworzy widgety """
        self.key1 = Button(self, text="0.01 zł ", font=("Courier",15,"bold"),
                           background="red", command=lambda: self.wrzuc(0.01, X))                                          #, command=lambda: self.keys_operation(1)
        self.key1.grid(row=0, column=0, sticky=W)

        self.key2 = Button(self, text="0.02 zł", font=("Courier",15,"bold"), background="red")
        self.key2.grid(row=0, column=1, sticky=W)

        self.key3 = Button(self, text="0.05 zł", font=("Courier",15,"bold"), background="red")
        self.key3.grid(row=0, column=2, sticky=W)

        self.key4 = Button(self, text="0.1 zł  ", font=("Courier",15,"bold"), background="red")
        self.key4.grid(row=1, column=0, sticky=W)

        self.key5 = Button(self, text="0.2 zł ", font=("Courier",15,"bold"), background="red")
        self.key5.grid(row=1, column=1, sticky=W)

        self.key6 = Button(self, text="0.5 zł ", font=("Courier",15,"bold"), background="red")
        self.key6.grid(row=1, column=2, sticky=W)

        self.key7 = Button(self, text="1.0 zł  ", font=("Courier",15,"bold"), background="red")
        self.key7.grid(row=2, column=0, sticky=W)

        self.key8 = Button(self, text="2.0 zł ", font=("Courier",15,"bold"), background="red")
        self.key8.grid(row=2, column=1, sticky=W)

        self.key9 = Button(self, text="5.0 zł ", font=("Courier",15,"bold"), background="red")
        self.key9.grid(row=2, column=2, sticky=W)

        self.wroc = Button(self, text="           Wróć          ", font=("Courier",15,"bold"), background="blue")
        self.wroc.grid(row=3, column=0, columnspan=3, sticky=W)

    def wrzuc(self, coin, X):
        """Metoda zwracająca pieniążek"""
        self.coins = coin

        print(self.coins)
        X.quit()
        X.destroy()
