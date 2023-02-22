from tkinter import filedialog
import os

class GetData:
    def __init__(self):
        pass

    def get_values(self, filePath):
        version = self.check_version(filePath)

        with open(filePath, "r", encoding="utf-8") as fOpen:

            lines = fOpen.read()

            match version:
                case 1:
                    print(1)                    
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
                        price = subject[subject.find("<Cena>")+6:subject.find("</Cena>")]
                        priceNetto = subject[subject.find("<WartoscNetto>")+14:subject.find("</WartoscNetto>")]
                        priceVat = subject[subject.find("<WartoscVAT>")+12:subject.find("</WartoscVAT>")]
                        vat = subject[subject.find("<Procent>")+9:subject.find("</Procent>")][1:]
                        amount = subject[subject.find("<Ilosc>")+7:subject.find("</Ilosc>")]
                        group = "Grupa Główna"

                        lines = lines[subjectEnd+10:]

                        print(index, description, unit, price, priceNetto, priceVat, vat, amount)

                case 2:
                    print(2)
                    amountOfSubjects = lines[lines.find("<LiczbaPozycji>")+15:lines.find("</LiczbaPozycji>")]
                    nip = "6970011183"

                    for subject in range(int(amountOfSubjects)):

                        subjectStart = lines.find("<Pozycja>")
                        subjectEnd = lines.find("</Pozycja>")
                        subject = lines[subjectStart:subjectEnd]

                        description = subject[subject.find("<Opis>")+6:subject.find("</Opis>")]
                        index = subject[subject.find("<Indeks>")+8:subject.find("</Indeks>")]
                        unit = subject[subject.find("<Jednostka>")+11:subject.find("</Jednostka>")]
                        price = subject[subject.find("<CenaPLN>")+9:subject.find("</CenaPLN>")]
                        priceNetto = subject[subject.find("<WartoscNetto>")+14:subject.find("</WartoscNetto>")]
                        vat = subject[subject.find("<Procent>")+9:subject.find("</Procent>")][:2]
                        amount = subject[subject.find("<Ilosc>")+7:subject.find("</Ilosc>")]
                        group = "Grupa Główna"

                        vatFloat = "0.{}".format(vat)
                        priceVat = "{:.2f}".format(float(priceNetto.replace(",", ".")) * float(vatFloat))

                        lines = lines[subjectEnd+10:]

                        print(index, description, unit, price, priceNetto, priceVat, vat, amount)


                case 3:
                    print(3)

                    nip = "firma_3"
                    amountOfSubjects = lines.count("<wiersz lp=")
                    rows = lines[lines.find("<wiersze>"):lines.find("</wiersze>")]

                    for subject in range(int(amountOfSubjects)):

                        subjectStart = rows.find("<wiersz")
                        subjectEnd = rows.find("</wiersz>")
                        subject = rows[subjectStart:subjectEnd]

                        description = subject[subject.find("<opisProduktu>")+14:subject.find("</opisProduktu>")]
                        index = subject[subject.find("<indeks>")+8:subject.find("</indeks>")]
                        unit = subject[subject.find("<jednostka>")+11:subject.find("</jednostka>")]                          
                        price = subject[subject.find("<cenaJednPrzedRabatem>")+22:subject.find("</cenaJednPrzedRabatem>")]
                        priceNetto = subject[subject.find("<kwotaNetto>")+12:subject.find("</kwotaNetto>")].replace(",", ".")
                        priceVat = subject[subject.find("<kwotaVAT>")+10:subject.find("</kwotaVAT>")].replace(",", ".")
                        vat = subject[subject.find("<kodVAT>")+10:subject.find("</kodVAT>")]
                        amount = subject[subject.find("<ilosc>")+7:subject.find("</ilosc>")]  
                        group = "Grupa Główna"

                        rows = rows[subjectEnd+7:]

                        print(index, description, unit, price, priceNetto, priceVat, vat, amount)

    def check_version(self, filePath):
        with open(filePath, "r", encoding="utf-8") as fOpen:
            lines = fOpen.read()

            if "<NIP>" in lines:
                seller = lines[lines.find('<StronaUmowy kto="Sprzedajacy">'):lines.find("</StronaUmowy>")]
                nip = seller[seller.find("<NIP>")+5:seller.find("</NIP>")].replace("-", "")
                print(nip)

                if nip == "7741008197":
                    version = 1
                elif nip == "6970011183":
                    version = 2

            elif "<wiersz lp=" in lines and "<nazwaNabywcy>ZAKTIM F.P.U.H.</nazwaNabywcy>" in lines:
                version = 3

        return version
   

        
            

    