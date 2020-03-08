class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, nisn, sma, hobi):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
        self.hobi= hobi
    def __str__(self):
        return "\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nHobi   : "+self.hobi\
               
    def ambilNama(self):
        print (self.nama)
    def ambilNISN(self):
        print (self.nisn)
    def ambilSma(self):
        print (self.sma)
    def ambilHobi(self):
        print (self.hobi)
