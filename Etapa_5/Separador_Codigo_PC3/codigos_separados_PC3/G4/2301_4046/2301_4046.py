from math import *

#Leitura
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))
angulo = float(input("Digite o valor do angulo entre o lado b e o lado c: "))

#Cálculo:
a = sqrt(((b ** 2) + (c ** 2)) - (2 * b * c * radians(cos(angulo))))

#Impressão:
print(round(a, 2))