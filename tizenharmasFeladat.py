'''
13.	Tárolj el 2 számot egy-egy változóba, ami egy téglalap két oldala. Írd ki a téglalap kerületét és területét!
'''
import beolvas

egyikOldal = beolvas.egeszSzamBeolvas()
masikOldal = beolvas.egeszSzamBeolvas()

kerulet = (egyikOldal + masikOldal) * 2 # (a + b) * 2
terulet = (egyikOldal * masikOldal) # (a * b)

print("A téglalap kerülete: " + str(kerulet))
print("A téglalap területe: " + str(terulet))
