from math import tan, pi
lado = float(input("tamanho do lado"))

b = 2*tan(pi/11)
apotema = lado/b

areaundecagono = (11*lado*apotema)/2

print(round(areaundecagono, 2))


# faça seu código aqui!