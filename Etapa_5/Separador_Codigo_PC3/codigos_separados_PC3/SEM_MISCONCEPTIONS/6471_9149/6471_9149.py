from math import tan, pi

# faça seu código aqui!
lado= float(input("lado: "))
apotema= lado / (2 * tan(pi/8))

area= 4 * lado * apotema

print(round(area, 2))



