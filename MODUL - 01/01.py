a = ""
bar = 1

x = int(input("Masukkan angka :"))


while bar <= x:
	kol = bar

	
	while kol > 0:
		a = a + " * "
		kol = kol - 1
		
	a = a + "\n"
	bar = bar + 1
print (a)
