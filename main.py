enterNumber = int(input("enter your number: "))
startNumber = 2
primeList = []
while True:

    if startNumber > 1:
        for i in range(2,startNumber):
            if (startNumber % i) == 0:
                break
        else:
            primeList.append(startNumber)
    if (len(primeList) == enterNumber):
        print(primeList)
        break
    else:
        startNumber = startNumber + 1
        continue