def binary (kumpulan,target):
    low = 0
    high = len(kumpulan) -1

    while low <= high:
        mid = (high + low) // 2
        if kumpulan [mid] == target:
            return "target berada di index " + str(mid)
            break
        
        elif target < kumpulan [mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False

listnya = [23, 51, 78, 10, 62, 145, 410]
target1 = 56
target2 = 62

print("listnya adalah ",listnya)
print("nilai target adalah ", target1)
print(binary(listnya, target1))

print("\nlistnya adalah ",listnya)
print("nilai target adalah ", target2)
print(binary(listnya, target2))
