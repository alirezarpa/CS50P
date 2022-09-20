print("Amount due: 50")

changeOwed = 50


while changeOwed > 0:
    coins = int(input("Insert coins: "))

    if coins < 0:
        print("Amount due: 50")

    if coins == 25 or coins == 10 or coins == 5:
        changeOwed -= coins
        if changeOwed <= 0:
            break
            print(0)
        print("Change owed: " + str(changeOwed))
    else:
        print(50)

#return absolute value returned
print("Change owed: " + str(abs(changeOwed)))