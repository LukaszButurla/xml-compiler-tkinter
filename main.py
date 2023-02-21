from tkinter import Tk
import customtkinter

class MainWindow:
    def __init__(self):
        self.create_window()

    def create_window(self):
        root = customtkinter.CTk()
        root.title("Konwerter XML")
        root.geometry("1280x720")
        root.mainloop()

if __name__ == "__main__":
    MainWindow()
        