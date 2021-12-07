import random

a = []
b = []
c = []

while True:
    volba = input("Pridaj (p), vypíš jeden zoznam (v), vypíš všetky zoznamy a ukonči (s):")

    x = random.randrange(1, 4)
    if x == 1:
        zoznam = a
    elif x == 2:
        zoznam = b
    else:
        zoznam = c

    if volba == "p":
        meno = input("ake meno? :")
        zoznam.append(meno)

    elif volba == "v":
        volba2 = input("aky list ?:")
        if volba2 == "a":
            print(a)
        elif volba2 == "b":
            print(b)
        elif volba2 == "c":
            print(c)
        else:
            break


    elif volba == "s":
        for i in a, b, c:
            print(i)
        break

    else:
        print("vybral si zle")
        break