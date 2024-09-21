'''
21.	Ments el két törtszámot két változóba, vond ki őket, majd írd ki egészre kerekített értéküket.
'''
import beolvas

szam1 = beolvas.tortSzamBeolvas() # 2.3
szam2 = beolvas.tortSzamBeolvas() # 5

kulonbseg = szam1 - szam2 # (2.3 - 5) = -2.7 kerekítve: -2

# Egész rész kiírása (kerekítés nélkül)
egesz_resz = int(kulonbseg)

print("A két törtszám különbségének egész része:", egesz_resz)