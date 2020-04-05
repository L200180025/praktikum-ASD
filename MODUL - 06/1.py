import mahasiswa as mhs

c1=mhs.mhsTIF("Rina",21,"Boyolali",240000)
c2=mhs.mhsTIF("Dina",22,"Klaten",220000)
c3=mhs.mhsTIF("Airin",23,"Jogja",260000)
c4=mhs.mhsTIF("Nabila",24,"Klaten",250000)
c5=mhs.mhsTIF("Himeyi",25,"Magelang",240000)
c6=mhs.mhsTIF("Kokura",26,"Jakarta",250000)
c7=mhs.mhsTIF("Momura",27,"Solo",220000)

x = [c1, c2, c3, c4, c5, c6, c7]


def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        kiri = a[:mid]
        kanan = a[mid:]

        merge(kiri)
        merge(kanan)

        i = 0;
        j = 0;
        k = 0
        while (i < len(kiri) and j < len(kanan)):
            if kiri[i].uang < kanan[j].uang:
                a[k] = kiri[i]
                i = i + 1
            else:
                a[k] = kanan[j]
                j = j + 1
            k = k + 1

        while i < len(kiri):
            a[k] = kiri[i]
            i = i + 1
            k = k + 1

        while j < len(kanan):
            a[k] = kanan[j]
            j = j + 1
            k = k + 1

def partition( arr, low, high):
    i = (low - 1)
    pivot = arr[high].uang
    for j in range(low, high):
        if arr[j].uang <= pivot:
            i = i + 1
            arr[i].uang, arr[j].uang = arr[j].uang, arr[i].uang
    arr[i + 1].uang, arr[high].uang = arr[high].uang, arr[i + 1].uang
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


merge(x)
for i in x:
    print(i.uang)

print("================================================")
quickSort(x,0,len(x)-1)
for i in x:
    print(i.uang)
