from tkinter import *

class Maschine(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        super(Maschine, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Utwórz widget dla Text dla wyświetlania komunikatu
        self.products = Text(self, width=25, height=30, wrap=WORD)
        self.products.grid(row=0, column=0, columnspan=2, rowspan=35, sticky=W)
        self.fill_products()

        # Keypad
        self.key1 = Button(self, text=" 1 ")                  #, command=self.reveal
        self.key1.grid(row=5, column=3, sticky=W)

        self.key2 = Button(self, text=" 2 ")  # , command=self.reveal
        self.key2.grid(row=5, column=4, sticky=W)

        self.key3 = Button(self, text=" 3 ")  # , command=self.reveal
        self.key3.grid(row=5, column=5, sticky=W)

        self.key4 = Button(self, text=" 4 ")  # , command=self.reveal
        self.key4.grid(row=6, column=3, sticky=W)

        self.key5 = Button(self, text=" 5 ")  # , command=self.reveal
        self.key5.grid(row=6, column=4, sticky=W)

        self.key6 = Button(self, text=" 6 ")  # , command=self.reveal
        self.key6.grid(row=6, column=5, sticky=W)

        self.key7 = Button(self, text=" 7 ")  # , command=self.reveal
        self.key7.grid(row=7, column=3, sticky=W)

        self.key8 = Button(self, text=" 8 ")  # , command=self.reveal
        self.key8.grid(row=7, column=4, sticky=W)

        self.key9 = Button(self, text=" 9 ")  # , command=self.reveal
        self.key9.grid(row=7, column=5, sticky=W)

        self.key0 = Button(self, text=" 0 ")  # , command=self.reveal
        self.key0.grid(row=8, column=4, sticky=W)




    def fill_products(self):
        """Wypełnienie listy produktów"""
        pr = ["jajka", "kiełba", "chuj"]
        lista = ""
        count =1
        for i in pr:
            lista += str(count) + ". " + i + "\n"
            count += 1

        self.products.insert(0.0, lista)