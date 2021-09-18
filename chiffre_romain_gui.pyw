import tkinter as tk
from tkinter.constants import END
from romainconverter import romain
from pyautogui import alert


class app_converter:
    def __init__(self):
        self.root = tk.Tk()

    def __convert_number(self):

        self.label.delete(0, END)
        converter = romain()

        if self.entry.get() == "":
            return

        try:
            converted = int(self.entry.get())
            self.label.insert(0, converter.convert(converted))
        except:
            alert("It's not a valid Number !")
        return

    def __initialize(self):
        icon = tk.PhotoImage(
            file=r"C:\Users\Amyr\Documents\python project gui\chiffre romain converter\romain.png")
        self.root.tk.call('wm', 'iconphoto', self.root, icon)
        self.root.title("Chiffre Romain Converter")
        self.root.configure(background="#FFB266")
        self.root.geometry("440x60")

        self.entry = tk.Entry(self.root)
        self.label = tk.Entry(self.root)
        self.button = tk.Button(
            self.root, text="Convert", command=self.__convert_number, width=10, background="#9999FF")

        self.entry.grid(row=0, column=0, padx=(40, 20), pady=(20, 20))
        self.label.grid(row=0, column=1)
        self.button.grid(row=0, column=2, padx=(20, 20))

    def start(self):
        self.__initialize()
        self.root.mainloop()


app = app_converter()
app.start()
