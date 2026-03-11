from math import tan, pi
compLadoP=float(input("lado do pentagono: "))
apotema=compLadoP/(2*tan(pi/5))
aP=(5*compLadoP*apotema)/2
print(round(aP,2))
