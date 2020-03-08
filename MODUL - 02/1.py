class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakKapital(self):
        print(str.upper(self.teks))
    def cetakKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlah(self):
        print("Kalimatku mempunyai: ",len(self.teks),"karakter")
    def perbarui(self, strBaru):
        self.teks = strBaru

    def apaTerkandung(self, isi):
        if str(isi) in self.teks:
            print("true")
        else:
            print("false")
    def hitungV(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i in v:
                n+=1
        return n

    def hitungK(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i not in v:
                n+=1
        return n
