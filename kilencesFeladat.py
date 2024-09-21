'''
9.	Tárolj el egy egész számot egy változóba! Növeld meg a változó tartalmát 15-tel, majd írd ki az értékét!
'''

import beolvas

szam1 = beolvas.egeszSzamBeolvas()

szam1 = szam1 + 15  # vagy szam1 += 15

print("A szám új értéke: " + str(szam1))


