import customtkinter

class Ui:
    def __init__(self, app):
        self.create_widgets(app)

    def create_widgets(self, app):
#--------------create grid frames-------------------------------------
        inputFrame = customtkinter.CTkFrame(app, width=640, height=90, fg_color="red")
        inputFrame.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE")

        outputFrame = customtkinter.CTkFrame(app, width=640, height=90, fg_color="yellow")
        outputFrame.grid(row = 0, column = 3, columnspan = 3, sticky = "NSWE")

        tableFrame = customtkinter.CTkFrame(app, width=1280, height=540, fg_color="green")
        tableFrame.grid(row = 1, column = 0, columnspan = 6, rowspan = 6, sticky = "NSWE")

        infoFrame = customtkinter.CTkFrame(app, width=120, height=90, fg_color="purple")
        infoFrame.grid(row = 7, column = 0, columnspan = 2, sticky = "NSWE")

        buttonFrame = customtkinter.CTkFrame(app, width=240, height=90, fg_color="brown")
        buttonFrame.grid(row = 7, column = 2, columnspan = 2, sticky = "NSWE")

        emptyFrame = customtkinter.CTkFrame(app, width=120, height=90, fg_color="orange")
        emptyFrame.grid(row = 7, column = 4, columnspan = 2, sticky = "NSWE")

#---------------configure grid----------------------------------------------

        app.columnconfigure((0,1,2,3,4,5), weight=1)
        app.rowconfigure((0, 7), weight = 2)
        app.rowconfigure((1,2,3,4,5,6), weight = 3)

