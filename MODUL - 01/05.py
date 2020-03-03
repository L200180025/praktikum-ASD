from math import sqrt as sq
def apakahPrima(x):
    x = int(x)
    primaKecil = [2,3,5,7,11]
    bknPrimaKecil = [0,1,4,6,8,9,10]
    if x in primaKecil:
        return True
    elif x in bknPrimaKecil:
        return False
    else:
        for i in range(2, int(sq(x))+1):
            if x % i == 0:
                return False
            else:
                return True
