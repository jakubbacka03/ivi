import random

a = []
b = []
c = []

while True:
    volba = input("Pridaj (p), vypíš jeden zoznam (v), vypíš všetky zoznamy a ukonči (s):")

    if volba == "p":
        meno = input("ake meno? :")
        a.append(meno)





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