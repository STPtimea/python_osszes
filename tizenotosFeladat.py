'''
15.	Tárolj el 3 számot egy-egy változóba! Írd ki a középső számot az értékük szerint összehasonlítva!
'''

import beolvas

szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

# A középső szám meghatározása
if (szam1 > szam2 and szam1 < szam3) or (szam1 > szam3 and szam1 < szam2):
    kozepso = szam1
elif (szam2 > szam1 and szam2 < szam3) or (szam2 > szam3 and szam2 < szam1):
    kozepso = szam2
else:
    kozepso = szam3

# Eredmény kiírása
print("A középső szám: " + str(kozepso))
