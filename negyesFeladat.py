import beolvas

szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

# Első lehetőség
print("1.szám: " + str(szam1)+"\n2.szám: "+str(szam2)+"\n3. szám:" + str(szam3))
# Második lehetőség
print("1.szám: "+ str(szam1), end="")
print("2.szám: "+ str(szam1), end="")
print("3.szám: "+ str(szam1))