'''
12.	Tárolj el egy egész számot egy változóba, ami egy kör átmérője. Írd ki a kör kerületét és területét!
'''
import beolvas
atmero = beolvas.egeszSzamBeolvas()

pi = 3.14
sugar = atmero / 2
kerulet = 2 * pi * sugar # vagy kerulet = pi * atmero
# Kör területe (Pi * sugár négyzeten)
terulet = pi * sugar * sugar # vagy terulet = pi * (sugar ** 2)

print("A kör kerülete: " + str(kerulet))
print("A kör területe: " + str(terulet))
