'''
18.	Ments el egy számot szövegként egy változóba, majd egy másik változóba egy egész számot. Majd írd ki az összegüket.
'''
import beolvas

szam1 = str(beolvas.egeszSzamBeolvas())
szam2 = beolvas.egeszSzamBeolvas()

# Szövegként tárolt számot egész számra konvertáljuk
osszeg = int(szam1) + szam2

print("A két szám összege: " + str(osszeg))

