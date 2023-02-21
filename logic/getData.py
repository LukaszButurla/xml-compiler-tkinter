from tkinter import filedialog

class GetData:
    def __init__(self):
        pass

    def select_file(self):
        selectedFile = filedialog.askopenfilename(filetypes=[("XML", ".xml")])


    