'''
14.	Tárolj el 3 számot egy-egy változóba! Írd ki a számtani közepüket!
'''
import beolvas

szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

atlag = (szam1 + szam2 + szam2) / 3

print("A három szám számtani közepe (átlaga): " + str(atlag))
