class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

        
c0 = Mahasiswa('Rina',10,'Boyolali',240000)
c1 = Mahasiswa('Dina',51,'Surabaya',230000)
c2 = Mahasiswa('Gilmore',2,'Whirlpool',250000)
c3 = Mahasiswa('Sanchez',18,'Andromeda',235000)
c4 = Mahasiswa('Morphine',4,'Semarang',240000)
c5 = Mahasiswa('Nabila',31,'Salatiga',250000)
c6 = Mahasiswa('Anna',13,'Klaten',245000)
c7 = Mahasiswa('Elsa',5,'Wonogiri',245000)
c8 = Mahasiswa('Olaf',23,'Klaten',245000)
c9 = Mahasiswa('Luffy',64,'Pekalongan',270000)
c10 = Mahasiswa('Conan',29,'Yogyakarta',230000)

angka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(angka)
print(angka)
