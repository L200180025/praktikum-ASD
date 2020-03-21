class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class buatArray(object):
    #membuat list
    internalData = 11*[None]

    #mengambil data di list
    def __getitem__(self, item):
        return self.internalData[item]

    #mengatur posisi data dan index-nya pada list
    def __setitem__(self, key, value):
        self.internalData[key] = value

    #03
    def cariuangkecil250k(self):
        terkecil = 250000
        d = []
        for i in self:
            if i.uangSaku < terkecil:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        for i in d:
            print (i)

c = buatArray()
c[0] = MhsTIF('Ika', 10, 'Sukoharjo', 2400000)
c[1] = MhsTIF('Budi', 51, 'Sragen', 2300000)
c[2] = MhsTIF('Ahmad', 2, 'Surakarta', 2500000)
c[3] = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c[4] = MhsTIF('Eka', 4, 'Boyolali', 2400000)
c[5] = MhsTIF('Fandi', 31, 'Salatiga', 2500000)
c[6] = MhsTIF('Deni', 13, 'Klaten', 2450000)
c[7] = MhsTIF('Galuh', 5, 'Wonogiri', 2450000)
c[8] = MhsTIF('Janto', 23, 'Klaten', 2450000)
c[9] = MhsTIF('Hasan', 64, 'Karanganyar', 2700000)
c[10] = MhsTIF('Khalid', 29, 'Purwodadi', 2650000)

#pengujian nomer 3
print ("Mahasiswa dengan uang saku kurang dari 250.000 adalah :")
c.cariuangkecil250k()
