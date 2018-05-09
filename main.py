from tkinter import *
from machine import Maschine

def main():
    try:
        root = Tk()
        root.title("Automat z napojami :)")
        root.geometry("400x550")

        app = Maschine(root)

        root.mainloop()
    except:
        print("Błąd w module main!!\nTworzenie okna głównego ")

if __name__=="__main__":
    main()
