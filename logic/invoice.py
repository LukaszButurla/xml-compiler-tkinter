import csv
import os

class Invoice:
    def __init__(self):
        pass
    
    def create_invoice(self, savePath, data, nip, name, number, fileName):
        fileName = "{}_faktura.xls".format(fileName)
        savePath = os.path.join(savePath, fileName)

        with open(savePath, "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=";")

            for d in data:
                values = [d[0], d[2], d[3]]
                writer.writerow(values)