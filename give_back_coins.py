from tkinter import *

class Give_Back_coins(Frame):
    def __init__(self, master, bc):
        """Inicjalizacja okno"""
        self.coins = bc
        super(Give_Back_coins, self).__init__(master)
        self.create_widgets(master)
        self.grid()

    def create_widgets(self, X):
        """Tworzy widgety """
        # Lista zwracanych monet
        self.coins_list = Text(self, width=25, height=22, font=("Courier", 13, "bold"), wrap=WORD)
        self.coins_list.grid(row=0, column=0, columnspan=2, rowspan=35, sticky=W)
        self.write_coins()

        self.wroc = Button(self, text="           Weź          ", font=("Courier", 15, "bold"),
                           background="purple", command=lambda: self.back(X))
        self.wroc.grid(row=20, column=0, columnspan=3, sticky=W)

    def write_coins(self):
        """Wypełnienie listy produktów"""
        lista = "Twoje monety :\n"
        for i in self.coins:
            lista += str(i) + "\n"

        self.coins_list.insert(0.0, lista)

    def back(self, X):
        """Ustal wartość pieniążka, zamyka okno"""
        X.quit()
        X.destroy()
