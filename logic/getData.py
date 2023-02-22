from tkinter import filedialog

class GetData:
    def __init__(self):
        pass

    def get_values(self, filePath):
        version = self.check_version(filePath)

    def check_version(self, filePath):
        with open(filePath, "r", encoding="utf-8") as fOpen:
            lines = fOpen.read()

            if "<NIP>" in lines:
                seller = lines[lines.find('<StronaUmowy kto="Sprzedajacy">'):lines.find("</StronaUmowy>")]
                nip = seller[seller.find("<NIP>")+5:seller.find("</NIP>")].replace("-", "")

                if nip == "7741008197":
                    version = 1
                elif nip == "6970011183":
                    version = 2

            elif "<wiersz lp=" in lines and "<nazwaNabywcy>ZAKTIM F.P.U.H.</nazwaNabywcy>" in lines:
                version = 3

        return version
   

        
            

    