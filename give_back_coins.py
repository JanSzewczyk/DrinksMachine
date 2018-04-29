from tkinter import *

class Give_Back_coins(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        super(Give_Back_coins, self).__init__(master)
        self.create_widgets(master)
        self.grid()

    def create_widgets(self, X):
        """Tworzy widgety """
        self.wroc = Button(self, text="           Weź          ", font=("Courier", 15, "bold"),
                           background="purple", command=lambda: self.back(X))
        self.wroc.grid(row=2, column=0, columnspan=3, sticky=W)

    def back(self, X):
        """Ustal wartość pieniążka, zamyka okno"""
        X.quit()
        X.destroy()
