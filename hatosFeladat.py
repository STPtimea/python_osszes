import beolvas
'''
6.	Tárolj el két számot egy-egy változóba! Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat teljes műveleti sorrendben.
Pl.:

Be: 3 2 számok esetén
Ki:
3-2=1
3+2=5
3*2=6
3/2=1,5
3^2=9
2^3=8
'''

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

osszeg = szam1 + szam2
kulonbseg = szam1-szam2
szorzat = szam1 * szam2
hanyados = szam1 / szam2
maradek = szam1 % szam2
hatvany = szam1 ** szam2
hatvany1 = szam1 ** szam2
hatvany2 = szam2 ** szam1

print(str(szam1) + "+" + str(szam2) + "=" + str(osszeg))
print(str(szam1) + "-" + str(szam2) + "=" + str(kulonbseg))
print(str(szam1) + "*" + str(szam2) + "=" + str(szorzat))
print(str(szam1) + "/" + str(szam2) + "=" + str(hanyados))
print(str(szam1) + "%" + str(szam2) + "=" + str(maradek))
print(str(szam1) + "^" + str(szam2) + "=" + str(hatvany1))
print(str(szam2) + "^" + str(szam1) + "=" + str(hatvany2))

