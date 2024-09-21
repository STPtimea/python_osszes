'''
7.	Tárolj el két számot egy-egy változóba! Írd ki az osztási maradékukat.
Be: 10 8
Ki: Osztási maradék: 2.
'''

import beolvas

szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

maradek = szam1 % szam2

print("Osztási maradék: " + str(maradek))
