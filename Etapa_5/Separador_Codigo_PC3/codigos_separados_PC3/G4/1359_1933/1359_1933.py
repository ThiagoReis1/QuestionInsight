from math import *
Ve = float(input("velocidade de exaustao:"))
Mo = float(input("massa inicial:"))
Mf = float(input("massa final:"))
DeltaV = Ve * log(Mo/Mf)
print(round(DeltaV,2))