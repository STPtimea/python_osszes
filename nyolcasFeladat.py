'''
8.	Tárolj el két számot egy-egy változóba! Egy harmadik változóba tárold el a két szám szorzatát, majd írasd ki a képernyőre!
'''

import beolvas

szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

szorzat = szam1 * szam2

print("A két szám szorzata: " + str(szorzat))
