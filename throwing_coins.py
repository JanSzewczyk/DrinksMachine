from tkinter import *

class Throwing_coins(Frame):
    def __init__(self, master):
        """Inicjalizacja okno"""
        self.coins = []
        super(Throwing_coins, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzy widgety """
        pass