from math import pi,tan
Ladoheptagono = float(input("digite o comprimento do lado do Heptagono: "))
apotema = Ladoheptagono/(2*tan(pi/7))
areaHeptagono = (7*Ladoheptagono*apotema)/2
print(round(areaHeptagono,2))
