from math import *
lado=input("quantidade de lados :")
a=(lado*7)
# faça seu código aqui!
apotema=(lado*tan) * (pi//7)
final=float(a*apotema/2)
print(round(final, 2))