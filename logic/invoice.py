import csv

class Invoice:
    def __init__(self):
        pass
    
    def create_invoice(self, savePath, data):
        with open(r"{}\test.xls".format(savePath), "w+", encoding="utf-8", newline="") as fSave:
            writer = csv.writer(fSave, delimiter=";")
            fSave.write("sep=;\n")

            for d in data:
                writer.writerow(d)