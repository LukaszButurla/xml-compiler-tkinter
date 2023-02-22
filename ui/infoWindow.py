from tkinter import Toplevel
from functools import partial
import customtkinter

class InfoWindow:
    def __init__(self, app, color, secondColor, textColor):
        self.app = app
        self.mainColor = color
        self.secondColor = secondColor
        self.textColor = textColor

    def open_window(self, text):
        window = Toplevel(self.app, background = self.mainColor)
        window.geometry("400x200")
        window.title("Informacja")
        window.minsize(400, 200)
        self.create_widgets(window, text)

    def create_widgets(self, window, text):
        labelInfo = customtkinter.CTkLabel(window, text=text, font = ("Arial", 19), text_color=self.textColor)
        labelInfo.grid(row = 0, column = 0, rowspan = 2, sticky = "NSWE")

        buttonCancel = customtkinter.CTkButton(window, text = "Ok", font = ("Arial", 19), fg_color=self.secondColor, command=partial(self.close_window, window))
        buttonCancel.grid(row = 2, column = 0, sticky = "NSWE", padx = 50, pady = 20)

        window.columnconfigure(0, weight = 1)
        window.rowconfigure((0, 1, 2), weight=1)

    def close_window(self, window):
        window.destroy()