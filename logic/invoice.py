import csv
import os

class Invoice:
    def __init__(self):
        pass
    
    def create_invoice(self, savePath, data, nip):
        fileName = "faktura_{}.xls".format(nip)
        savePath = os.path.join(savePath, fileName)

        with open(savePath, "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=";")
            fSave.write("sep=;\n")

            for d in data:
                writer.writerow(d)