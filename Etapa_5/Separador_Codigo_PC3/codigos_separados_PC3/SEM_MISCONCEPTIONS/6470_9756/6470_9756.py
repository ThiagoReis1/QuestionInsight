from math import *

# faça seu código aqui!
ladocomp = float(input("INFORME O COMPRIMENTO DO LADO DO HEPTAGONO: "))

apotema = ladocomp/(2*tan(pi/7))

area_hepta = ((7*ladocomp*apotema)/2)

print(round(area_hepta,2))


