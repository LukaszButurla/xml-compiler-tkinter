class Invoice:
    def __init__(self):
        pass
    
    def create_invoice(self, savePath, data):
        print(savePath)
        for d in data:
            print(d[0], d[1], d[2])