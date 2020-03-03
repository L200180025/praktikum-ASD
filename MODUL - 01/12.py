from random import randint
print("""Permainan tebak angka.
Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba Tebak!""")
a = randint(1, 100)
for i in range (3):
    b = int(input("Masukkan tebakkan ke-{}:>".format(i+1)))
    if b == a:
        print ("Ya. Anda benar.")
    elif b > a:
        if i >= 2:
            print ("Itu terlalu besar. Kesempatan habis. Nilainya adalah",a)
        else: 
            print ("Itu terlalu besar. Coba lagi")
    else:
        if i >= 2:
            print ("Itu terlalu kecil. Kesempatan habis. Nilainya adalah",a)
        else: 
            print ("Itu terlalu kecil. Coba lagi")
