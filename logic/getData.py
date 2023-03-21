from tkinter import filedialog, END
import os

class GetData:
    def __init__(self):
        pass

    def get_values(self, filePath, window, add_row_to_table, clear_table, summaryVat, summaryNetto, summarySubjects):
        version = self.check_version(filePath)        
        clear_table()

        with open(filePath, "r", encoding="utf-8") as fOpen:

            lines = fOpen.read()
            priceVatAll = 0.0
            priceNettoAll = 0.0
            amountOfSubjects = 0
            nip = 0
            detected = True

            match version:
                case 0:
                    window.open_window("Nie rozpoznano firmy")  
                    detected = False
                    
                case 1:
                    window.open_window("PONZIO POLSKA Sp. z o.o\nNip: 7741008197")                   
                    amountOfSubjects = lines[lines.find("<LiczbaPozycji>")+15:lines.find("</LiczbaPozycji>")]
                    nip = "7741008197"

                    for subject in range(int(amountOfSubjects)):

                        subjectStart = lines.find("<Pozycja>")
                        subjectEnd = lines.find("</Pozycja>")
                        subject = lines[subjectStart:subjectEnd]

                        description1 = subject[subject.find("<Opis>")+6:subject.find("</Opis>")]
                        descripton2 = subject[subject.find("<Opis1>")+7:subject.find("</Opis1>")]

                        description = "{} {}".format(description1, descripton2)
                        index = subject[subject.find("<Indeks>")+8:subject.find("</Indeks>")]
                        unit = subject[subject.find("<Jednostka>")+11:subject.find("</Jednostka>")]
                        price = "{:.2f}".format(float(subject[subject.find("<Cena>")+6:subject.find("</Cena>")].replace(",", ".")))
                        priceNetto = "{:.2f}".format(float(subject[subject.find("<WartoscNetto>")+14:subject.find("</WartoscNetto>")]))
                        priceVat = "{:.2f}".format(float(subject[subject.find("<WartoscVAT>")+12:subject.find("</WartoscVAT>")]))
                        vat = subject[subject.find("<Procent>")+9:subject.find("</Procent>")][1:]
                        amount = "{:.0f}".format(float(subject[subject.find("<Ilosc>")+7:subject.find("</Ilosc>")]))
                        priceVatAll += float(priceVat)
                        priceNettoAll += float(priceNetto)
                        
                        values = [index, description, amount, price, vat, priceVat, priceNetto, unit]
                        add_row_to_table(values)

                        lines = lines[subjectEnd+10:]

                case 2:
                    window.open_window("Winkhaus Polska Beteiligungs Sp. z o.o sp.k.\nNip: 6970011183") 
                    amountOfSubjects = lines[lines.find("<LiczbaPozycji>")+15:lines.find("</LiczbaPozycji>")]
                    nip = "6970011183"

                    for subject in range(int(amountOfSubjects)):

                        subjectStart = lines.find("<Pozycja>")
                        subjectEnd = lines.find("</Pozycja>")
                        subject = lines[subjectStart:subjectEnd]

                        description = subject[subject.find("<Opis>")+6:subject.find("</Opis>")]
                        index = subject[subject.find("<Indeks>")+8:subject.find("</Indeks>")]
                        unit = subject[subject.find("<Jednostka>")+11:subject.find("</Jednostka>")]
                        price = "{:.2f}".format(float(subject[subject.find("<CenaPLN>")+9:subject.find("</CenaPLN>")].replace(",", ".")))
                        priceNetto = "{:.2f}".format(float(subject[subject.find("<WartoscNetto>")+14:subject.find("</WartoscNetto>")].replace(",", ".")))
                        vat = subject[subject.find("<Procent>")+9:subject.find("</Procent>")][:2]
                        amount = "{:.0f}".format(float(subject[subject.find("<Ilosc>")+7:subject.find("</Ilosc>")]))

                        vatFloat = "0.{}".format(vat)
                        priceVat = "{:.2f}".format(float(priceNetto.replace(",", ".")) * float(vatFloat))

                        priceVatAll += float(priceVat)
                        priceNettoAll += float(priceNetto)

                        values = [index, description, amount, price, vat, priceVat, priceNetto, unit]
                        add_row_to_table(values)
                        lines = lines[subjectEnd+10:]

                case 3:
                    window.open_window("Aliplast") 

                    nip = "Aliplast"
                    amountOfSubjects = lines.count("<wiersz lp=")
                    rows = lines[lines.find("<wiersze>"):lines.find("</wiersze>")]

                    for subject in range(int(amountOfSubjects)):

                        subjectStart = rows.find("<wiersz")
                        subjectEnd = rows.find("</wiersz>")
                        subject = rows[subjectStart:subjectEnd]

                        description = subject[subject.find("<opisProduktu>")+14:subject.find("</opisProduktu>")]
                        index = subject[subject.find("<indeks>")+8:subject.find("</indeks>")]
                        unit = subject[subject.find("<jednostka>")+11:subject.find("</jednostka>")]                          
                        price = "{:.2f}".format(float(subject[subject.find("<cenaJednPrzedRabatem>")+22:subject.find("</cenaJednPrzedRabatem>")].replace(",", ".")))
                        priceNetto = "{:.2f}".format(float(subject[subject.find("<kwotaNetto>")+12:subject.find("</kwotaNetto>")].replace(",", ".")))
                        priceVat = "{:.2f}".format(float(subject[subject.find("<kwotaVAT>")+10:subject.find("</kwotaVAT>")].replace(",", ".")))
                        vat = subject[subject.find("<kodVAT>")+10:subject.find("</kodVAT>")]
                        amount = "{:.0f}".format(float(subject[subject.find("<ilosc>")+7:subject.find("</ilosc>")].replace(",", ".")))

                        priceVatAll += float(priceVat)
                        priceNettoAll += float(priceNetto)

                        values = [index, description, amount, price, vat, priceVat, priceNetto, unit]
                        add_row_to_table(values)
                        rows = rows[subjectEnd+7:]
                

        summarySubjects.configure(text = "Liczba przedmiotów:\n{}".format(amountOfSubjects))
        summaryVat.configure(text = "Podsumowanie wartość vat:\n{:.2f}".format(priceVatAll))
        summaryNetto.configure(text = "Podsumowanie wartość Netto:\n{:.2f}".format(priceNettoAll))
        return nip, detected

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
                
            else:
                version = 0

        return version