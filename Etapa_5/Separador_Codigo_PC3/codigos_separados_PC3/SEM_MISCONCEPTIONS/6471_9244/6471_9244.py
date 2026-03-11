from math import tan, pi

lado = int(input("digite aqui o tamanho do lado: "))

apotema = lado / (2 * tan (pi / 8))
calculo_area = 4 * lado * apotema 

print(round(calculo_area, 2))


