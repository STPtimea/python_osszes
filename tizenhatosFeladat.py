'''
16.	Tárolj el 2 számot egy-egy változóba, melyek egy derékszögű háromszög befogói. Mekkora a harmadik oldala?
'''
import beolvas

befogo1 = beolvas.egeszSzamBeolvas()
befogo2 = beolvas.egeszSzamBeolvas()
atfogo = (befogo1**2 + befogo2**2) ** 0.5

print("A derékszögű háromszög átfogója:" +str(atfogo))
# print(f"A derékszögű háromszög átfogója: {atfogo}")