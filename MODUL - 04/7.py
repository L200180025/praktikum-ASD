def binary (kumpulan,target):
    low = 0
    high = len(kumpulan) -1
    listku = []

    while low <= high:
        if kumpulan [low] == target:
            listku.append(low)
            low += 1
        else:
            low += 1
    return listku

s = [2,6,5,6,4,6,7,8,6,10,14,15]
dicari = 6
print("Posisi data ", dicari, " pada list ", s, "adalah ",binary(s, dicari))
