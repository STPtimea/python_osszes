# 1. a. feladat
egeszSzam = 5
print(egeszSzam)
print(type(egeszSzam))
print("Egész szám: " + str(egeszSzam)+".")  # Típus-kényszerítés

# 1. b. feladat
tortSzam = 4.7
print(tortSzam)
print(type(tortSzam))
print("Tört szám: " + str(tortSzam)+".")

# 1. c. feladat
szin = "Kék, zöld, szürke, fekete, fehér"
print(szin)
print(type(szin))
print("A kedvenc színem a", szin, ".")  # van szóköz kiíratásnál
print("A kedvenc színem a "+szin+".")  # Típus-kényszerítés

# 1. d. feladat
betu = 'a'
print(betu)
print(type(betu))
print("Az ABC első betűje: "+betu+".")

# 1. e. feladat
szunetvanE = True
print(szunetvanE)
print(type(szunetvanE))

# 1. f. feladat
szunetvanE = False
print(szunetvanE)
print(type(szunetvanE))

# 2.Tárolj el egy egész számot egy változóba! Írd ki a felét!
szam = 16
fele = int(szam / 2)
print("A(z) " + str(szam)+" szám fele "+str(fele)+".")

# 3.
szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg az második számot: "))
szam3 = int(input("Add meg a harmadik számot: "))

'''
print("1.szám: "+ str(szam1))
print("2.szám: "+ str(szam1))
print("3.szám: "+ str(szam1))
'''
print("1.szám: " + str(szam1)+"\n2.szám: "+str(szam2)+"\n3. szám:" + str(szam3))

# 4.Készíts egy programot, amely beolvas 3 valós számot, majd kiírja őket, mindegyiket egy sorba szóközzel elválasztva!

# Első lehetőség
print("1.szám: " + str(szam1)+"\n2.szám: "+str(szam2)+"\n3. szám:" + str(szam3))
# Második lehetőség
print("1.szám: " + str(szam1), end="")
print("2.szám: " + str(szam1), end="")
print("3.szám: " + str(szam1))
