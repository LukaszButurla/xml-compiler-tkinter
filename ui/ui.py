import customtkinter
from tkinter import filedialog
from functools import partial
from ui.infoWindow import InfoWindow

class Ui:
    def __init__(self, app, getData):
        mainColor = "#F8F4EA"
        secondColor = "#579BB1"
        thirdColor = "#ECE8DD"
        fourthColor = "#E1D7C6"
        self.infoWindow = InfoWindow(app, mainColor, secondColor)
        self.getData = getData
        self.create_widgets(app, mainColor, secondColor, thirdColor, fourthColor)

    def create_widgets(self, app, color, secondColor, thirdColor, fourthColor):
#--------------create grid frames-------------------------------------
        inputFrame = customtkinter.CTkFrame(app, width=640, height=72, fg_color=color, border_color=fourthColor, border_width=4)
        inputFrame.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE")

        outputFrame = customtkinter.CTkFrame(app, width=640, height=72, fg_color=color, border_color=fourthColor, border_width=4)
        outputFrame.grid(row = 0, column = 3, columnspan = 3, sticky = "NSWE")

        tableFrame = customtkinter.CTkFrame(app, width=1280, height=504, fg_color=thirdColor)
        tableFrame.grid(row = 1, column = 0, columnspan = 6, rowspan = 7, sticky = "NSWE")

        summaryFrame = customtkinter.CTkFrame(app, width=1280, height=72, fg_color=thirdColor, border_color=fourthColor, border_width=4)
        summaryFrame.grid(row = 8, column = 0, columnspan = 6, sticky = "NSWE")

        infoFrame = customtkinter.CTkFrame(app, width=120, height=72, fg_color=color)
        infoFrame.grid(row = 9, column = 0, columnspan = 2, sticky = "NSWE")

        buttonFrame = customtkinter.CTkFrame(app, width=240, height=72, fg_color=color)
        buttonFrame.grid(row = 9, column = 2, columnspan = 2, sticky = "NSWE")

        emptyFrame = customtkinter.CTkFrame(app, width=120, height=72, fg_color=color)
        emptyFrame.grid(row = 9, column = 4, columnspan = 2, sticky = "NSWE")

#---------------configure grid----------------------------------------------
        app.columnconfigure((0,1,2,3,4,5), weight=1)
        app.rowconfigure((0, 9), weight = 2, minsize = 72)
        app.rowconfigure((1,2,3,4,5,6, 7, 8), weight = 3)

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


#---------------add widgets----------------------------------------------
        inputInfoLabel = customtkinter.CTkLabel(inputFrame, text = "Ścieżka do pliku:", font = ("Arial", 20), anchor="nw", justify = "left")
        inputInfoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE", padx = 15, pady = 15)

        inputButton = customtkinter.CTkButton(inputFrame, text = "Wybierz", font = ("Arial", 19), fg_color=secondColor, command=partial(self.open_select_file_window, app, inputInfoLabel))
        inputButton.grid(row = 0, column = 3, sticky = "NSWE", padx = 15, pady = 15)

        outputInfoLabel = customtkinter.CTkLabel(outputFrame, text = "Ścieżka do Folderu:", font = ("Arial", 20), anchor="nw")
        outputInfoLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE", padx = 15, pady = 15)

        outputButton = customtkinter.CTkButton(outputFrame, text = "Wybierz", font = ("Arial", 19), fg_color=secondColor)
        outputButton.grid(row = 0, column = 3, sticky = "NSWE", padx = 15, pady = 15)

        infoButton = customtkinter.CTkButton(infoFrame, text = "O programie", font = ("Arial", 19), fg_color=secondColor)
        infoButton.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = "NSWE")

        convertButton = customtkinter.CTkButton(buttonFrame, text = "Potwierdź", font = ("Arial", 19), fg_color=secondColor)
        convertButton.grid(row = 0, column = 0, sticky= "NSWE", padx = 30, pady = 15)

        dataScrollFrame = customtkinter.CTkScrollableFrame(tableFrame, fg_color=thirdColor)
        dataScrollFrame.grid(sticky = "NSWE")


    def open_select_file_window(self, text, label):
        selectedFile = filedialog.askopenfilename(filetypes=[("XML", ".xml")])

        if selectedFile == "":
            pass
        elif selectedFile.endswith(".xml"):
            print("accept")
            label.configure(text = "Ścieżka do pliku:\n{}".format(selectedFile))
        else:
            self.infoWindow.open_window("Niepoprawny format pliku")




