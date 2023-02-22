import customtkinter

class infoPage:
    def __init__(self, frame):
        self.create_page(frame)

    def create_page(self, frame):
        print("open")
        
        self.infoFrame = customtkinter.CTkFrame(frame, fg_color="lightgreen")