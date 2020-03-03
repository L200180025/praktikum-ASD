def rubah35():
    a = 1
    b = 100
    for i in range (a, b+1):
        if (i % 3) == 0 and (i % 5) == 0:
            print ("Python UMS")
        elif (i % 3) == 0:
            print ("Python")
        elif (i % 5) == 0:
            print ("UMS")
        else:
            print (i)
