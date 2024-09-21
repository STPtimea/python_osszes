'''
20.	Ments el két törtszámot két változóba, add össze őket, majd írd ki egészre kerekített értéküket.
'''
import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

osszeg = szam1 + szam2

egesz_resz = int(osszeg)  # Az egész rész
tort_resz = osszeg - egesz_resz  # A törtrész

kerekitett_ertek = egesz_resz
if tort_resz >= 0.5:
    kerekitett_ertek += 1  # Ha a törtrész 0.5 vagy több, növeljük az egész részt

print("A két törtszám összege egészre kerekítve:", kerekitett_ertek)

'''
Másik megoldás
'''
import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()
osszeg = szam1 + szam2

# Ha nagyobb például: törtrész = 7.8 - 7 = 0.8 vagyis nagyobb, mint 0.5 akkor az egész számot 8-ra kerekítjük,
# Ha kisebb például: törtrész = 7.3 - 7 = 0.3 tehát kisebb mint 0.5 akkor az egész számot 7-re kerekítjük.
if osszeg - int(osszeg) >= 0.5:
    kerekitett_ertek = int(osszeg) + 1
else:
    kerekitett_ertek = int(osszeg)

print("A két törtszám összege egészre kerekítve:", kerekitett_ertek)