import customtkinter
from tkinter import filedialog, ttk, END
from functools import partial
from ui.infoWindow import InfoWindow
from ui.infoPage import infoPage
import os

class Ui:
    def __init__(self, app, getData, create_invoice):
        mainColor = "#F8F4EA"
        secondColor = "#579BB1"
        thirdColor = "#ECE8DD"
        fourthColor = "#E1D7C6"
        self.infoWindow = InfoWindow(app, mainColor, secondColor)
        self.getData = getData
        self.create_invoice = create_invoice
        self.infoPage = infoPage()
        self.create_widgets(app, mainColor, secondColor, thirdColor, fourthColor)



    def create_widgets(self, app, color, secondColor, thirdColor, fourthColor):
#--------------create grid frames-------------------------------------
        inputFrame = customtkinter.CTkFrame(app, width=640, height=72, fg_color=color, border_color=fourthColor, border_width=4)
        inputFrame.grid(row = 0, column = 0, rowspan = 2, columnspan = 3, sticky = "NSWE")

        outputFrame = customtkinter.CTkFrame(app, width=640, height=72, fg_color=color, border_color=fourthColor, border_width=4)
        outputFrame.grid(row = 0, column = 3, rowspan = 2, columnspan = 3, sticky = "NSWE")

        tableFrame = customtkinter.CTkFrame(app, width=1280, height=504, fg_color=thirdColor)
        tableFrame.grid(row = 2, column = 0, rowspan = 14, columnspan = 6, sticky = "NSWE")

        summaryFrame = customtkinter.CTkFrame(app, width=1280, height=36, fg_color=thirdColor)
        summaryFrame.grid(row = 16, column = 0, columnspan = 6, sticky = "NSWE")

        infoFrame = customtkinter.CTkFrame(app, width=120, height=72, fg_color=color)
        infoFrame.grid(row = 17, column = 0, rowspan = 2, columnspan = 2, sticky = "NSWE")

        buttonFrame = customtkinter.CTkFrame(app, width=240, height=72, fg_color=color)
        buttonFrame.grid(row = 17, column = 2, rowspan = 2, columnspan = 2, sticky = "NSWE")

        emptyFrame = customtkinter.CTkFrame(app, width=120, height=72, fg_color=color)
        emptyFrame.grid(row = 17, column = 4, rowspan = 2, columnspan = 2, sticky = "NSWE")

#---------------configure grid----------------------------------------------
        app.columnconfigure((0,1,2,3,4,5), weight=1)
        app.rowconfigure((0, 9, 8), weight = 2, minsize = 72)
        app.rowconfigure((1,2,3,4,5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight = 3)

        inputFrame.columnconfigure((0, 1, 2, 3), weight=1)
        inputFrame.rowconfigure(0, weight=1)

        outputFrame.columnconfigure((0, 1, 2, 3), weight=1)
        outputFrame.rowconfigure(0, weight=1)

        infoFrame.columnconfigure((0, 1, 2, 3), weight=1)
        infoFrame.rowconfigure(0, weight=1)

        buttonFrame.columnconfigure(0, weight=1)
        buttonFrame.rowconfigure(0, weight=1)

        tableFrame.columnconfigure(0, weight=1)
        tableFrame.rowconfigure(0, weight=1)

        summaryFrame.rowconfigure(0, weight=1)
        summaryFrame.columnconfigure((0,1, 2), weight=1)

#------------------------summary widgets----------------------------
        summarySubjectLabel = customtkinter.CTkLabel(summaryFrame, text = "Liczba przedmiotów:\n", font = ("Arial", 20), anchor="nw", justify = "right")
        summarySubjectLabel.grid(row = 0, column = 0, sticky = "NSWE", padx = 15)

        summaryVatLabel = customtkinter.CTkLabel(summaryFrame, text = "Podsumowanie wartość vat:\n", font = ("Arial", 20), anchor="nw", justify = "right")
        summaryVatLabel.grid(row = 0, column = 1, sticky = "NSWE", padx = 15)

        summaryNettoLabel = customtkinter.CTkLabel(summaryFrame, text = "Podsumowanie wartość Netto:\n", font = ("Arial", 20), anchor="nw", justify = "right")
        summaryNettoLabel.grid(row = 0, column = 2, sticky = "NSWE", padx = 15)


#---------------add widgets----------------------------------------------
        inputInfoLabel = customtkinter.CTkLabel(inputFrame, text = "Ścieżka do pliku:", font = ("Arial", 20), anchor="nw", justify = "left")
        inputInfoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE", padx = 15, pady = 15)
        outputInfoLabel = customtkinter.CTkLabel(outputFrame, text = "Ścieżka do Folderu:", font = ("Arial", 20), anchor="nw", justify = "left")
        inputButton = customtkinter.CTkButton(inputFrame, text = "Wybierz", font = ("Arial", 19), fg_color=secondColor, command=partial(self.select_file, inputInfoLabel, summaryVatLabel, summaryNettoLabel, summarySubjectLabel))

        inputButton.grid(row = 0, column = 3, sticky = "NSWE", padx = 15, pady = 15)
        outputInfoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE", padx = 15, pady = 15)

        outputButton = customtkinter.CTkButton(outputFrame, text = "Wybierz", font = ("Arial", 19), fg_color=secondColor, command=partial(self.open_select_folder_window, outputInfoLabel))
        outputButton.grid(row = 0, column = 3, sticky = "NSWE", padx = 15, pady = 15)

        infoButton = customtkinter.CTkButton(infoFrame, text = "O programie", font = ("Arial", 19), fg_color=secondColor, command=self.open_info_page)
        infoButton.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = "NSWE")

        convertButton = customtkinter.CTkButton(buttonFrame, text = "Potwierdź", font = ("Arial", 19), fg_color=secondColor, command=self.create_files)
        convertButton.grid(row = 0, column = 0, sticky= "NSWE", padx = 30, pady = 15)

        dataScrollFrame = customtkinter.CTkFrame(tableFrame, fg_color=thirdColor)
        dataScrollFrame.grid(sticky = "NSWE")    
        dataScrollFrame.columnconfigure(0, weight=1)
        dataScrollFrame.rowconfigure(0, weight=1)

#-----------------------------table with data-------------------------------
        columns = ("index", "description", "amount", "price", "vat", "price_vat", "price_netto")
        self.dataTreeview = ttk.Treeview(dataScrollFrame, columns=columns, show="headings")
        self.dataTreeview.heading("index", text="Index")
        self.dataTreeview.heading("description", text="Opis")
        self.dataTreeview.heading("amount", text="Ilość")
        self.dataTreeview.heading("price", text="Cena jednostkowa")
        self.dataTreeview.heading("vat", text="Vat")
        self.dataTreeview.heading("price_vat", text="Wartość vat")
        self.dataTreeview.heading("price_netto", text="Wartość netto")
        self.dataTreeview.grid(row = 0, column = 0, sticky = "NSWE", padx = 10, pady = 10)

#-----------------------------------style table------------------------------------
        s = ttk.Style()
        s.configure("Treeview",
                    font = ("Arial", 15),
                    rowheight = 20)
        s.configure("Treeview.Heading",
                   font=(None, 16))
        
        self.dataTreeview.column("# 1", width=75)
        self.dataTreeview.column("# 2", width=350)
        self.dataTreeview.column("# 3", width=75, anchor="e")
        self.dataTreeview.column("# 4", width=125, anchor="e")
        self.dataTreeview.column("# 5", width=75, anchor="e")
        self.dataTreeview.column("# 6", width=100, anchor="e")
        self.dataTreeview.column("# 7", width=100, anchor="e")


    def open_select_file_window(self, label):
        self.selectedFile = filedialog.askopenfilename(filetypes=[("XML", ".xml")])

        if self.selectedFile == "":
            pass
        elif self.selectedFile.endswith(".xml"):
            print("accept")
            label.configure(text = "Ścieżka do pliku:\n{}".format(self.selectedFile))
        else:
            self.infoWindow.open_window("Niepoprawny format pliku")

        return self.selectedFile
    
    def add_row_to_table(self, values):
        self.dataTreeview.insert('', END, values=values)

    def clear_table(self):
        self.dataTreeview.delete(*self.dataTreeview.get_children())

    def open_select_folder_window(self, label):
        self.selectedFolder = filedialog.askdirectory()

        if self.selectedFolder == "":
            pass
        else:
            label.configure(text = "Ścieżka do katalogu:\n{}".format(self.selectedFolder))     

    def open_info_page(self):
        self.infoPage.open_page()       

    def select_file(self, label, summaryVat, summaryNetto, summarySubjects):
        filePath = self.open_select_file_window(label)
        self.nip = self.getData.get_values(filePath, self.infoWindow, self.add_row_to_table, self.clear_table, summaryVat, summaryNetto, summarySubjects)
        print(self.nip)

    def create_files(self):

        data = []

        for row in self.dataTreeview.get_children():
            values = self.dataTreeview.item(row).get("values")
            index = values[0]
            price = values[3]
            amount = values[2]

            data.append([index, amount, price])
            
        self.create_invoice(self.selectedFolder, data, self.nip)




