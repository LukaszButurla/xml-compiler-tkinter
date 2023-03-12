import csv
import os

class Invoice:
    def __init__(self):
        pass
    
    def create_invoice(self, savePath, data, nip):
        fileName1 = "faktura_{}_,_stary.xls".format(nip)
        savePath1 = os.path.join(savePath, fileName1)

        with open(savePath1, "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=",")

            for d in data:
                values = [d[0], d[2], d[3]]
                writer.writerow(values)
                
        fileName2 = "faktura_{}_;_stary.xls".format(nip)
        savePath2 = os.path.join(savePath, fileName2)

        with open(savePath2, "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=";")

            for d in data:
                values = [d[0], d[2], d[3]]
                writer.writerow(values)
                
        fileName3 = "faktura_{}_;_nowy.xls".format(nip)
        savePath3 = os.path.join(savePath, fileName3)
        
        with open(savePath3, "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=";")

            for d in data:
                values = [d[0], d[2], d[3].replace(",", ".")]
                writer.writerow(values)
                
                

                