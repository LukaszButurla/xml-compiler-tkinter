from tkinter import Tk
import customtkinter
from ui.ui import Ui
from logic.getData import GetData

class MainWindow:
    def __init__(self):
        self.create_window()
        self.import_classes()
        self.root.mainloop()

    def import_classes(self):
        self.getData = GetData()
        self.ui = Ui(self.root, self.getData)

    def create_window(self):
        self.root = customtkinter.CTk()
        self.root.title("Konwerter XML")
        self.root.geometry("1280x720")
        self.root.minsize(750, 300)

if __name__ == "__main__":
    MainWindow()
        