import customtkinter

class infoPage:
    def __init__(self, frame, mainColor, secondColor, thirdColor, fourthColor):
        self.create_page(frame, mainColor, secondColor, thirdColor, fourthColor)

    def create_page(self, frame, mainColor, secondColor, thirdColor, fourthColor):
        
        self.infoFrame = customtkinter.CTkFrame(frame, fg_color=mainColor)
        self.infoFrame.columnconfigure((0, 1, 2), weight=1)
        self.infoFrame.rowconfigure((0, 1, 2, 3), weight=2)
        self.infoFrame.rowconfigure(4, weight=1)
        
        companies = "PONZIO POLSKA Sp. z o.o\nNip: 7741008197\n\nWinkhaus Polska Beteiligungs Sp. z o.o sp.k.\nNip: 6970011183\n\nAliplast"
        
        companiesFrame = customtkinter.CTkFrame(self.infoFrame, fg_color=thirdColor)
        companiesFrame.grid(row = 0, column = 0, rowspan = 4, columnspan = 3, sticky = "NSWE", padx = 50, pady = 50)
        
        companiesFrame.rowconfigure(0, weight=1)
        companiesFrame.columnconfigure(0, weight=1)
                
        companiesLabel = customtkinter.CTkLabel(companiesFrame, text = companies, font=("Arial", 25))
        companiesLabel.grid(row = 0, column = 0, sticky = "NSWE")
        
        exitButton = customtkinter.CTkButton(self.infoFrame, text = "Wyjdź")
        exitButton.grid(row = 4, column = 1, sticky = "NSWE", padx = 50, pady = 50)
        