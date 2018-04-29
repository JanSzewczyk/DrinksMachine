from tkinter import *
from machine import Maschine

def main():
    root = Tk()
    root.title("Automat z napojami :)")
    root.geometry("400x550")

    app = Maschine(root)

    root.mainloop()

if __name__ == "__main__":
    main()
