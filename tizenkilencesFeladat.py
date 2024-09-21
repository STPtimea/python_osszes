'''
19.	Tárolj el egy kétjegyű egész számot egy változóba! Írd ki a számjegyek összegét!
'''
import beolvas

# Kétjegyű szám beolvasása
szam = beolvas.egeszSzamBeolvas()

# Számjegyek kinyerése
tizes = szam // 10
egyed = szam % 10

# Számjegyek összege
osszeg = tizes + egyed

# Eredmény kiírása
print("A számjegyek összege:", osszeg)
