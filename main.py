from tkinter import Tk
import customtkinter
from ui.ui import Ui
from logic.getData import GetData
from logic.invoice import Invoice
from logic.priceList import PriceList


class MainWindow:
    def __init__(self):
        self.create_window()
        self.import_classes()
        self.root.mainloop()

    def import_classes(self):
        self.getData = GetData()
        self.invoice = Invoice()
        self.priceList = PriceList()
        self.ui = Ui(self.root, self.getData, self.invoice.create_invoice, self.priceList.create_invoice)

    def create_window(self):
        self.root = customtkinter.CTk()
        self.root.title("Konwerter XML")
        self.root.geometry("1280x720")
        self.root.minsize(750, 300)

if __name__ == "__main__":
    MainWindow()
        