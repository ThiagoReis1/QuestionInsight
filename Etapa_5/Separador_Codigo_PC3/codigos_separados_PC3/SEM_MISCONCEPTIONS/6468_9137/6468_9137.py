from math import tan, pi

comprimento = float(input("Digite o comprimento do lado: "))
lado = comprimento
apotema = lado / (2 * tan(pi / 5))
area_pent = (5 * lado * apotema) / 2
print(round(area_pent, 2))