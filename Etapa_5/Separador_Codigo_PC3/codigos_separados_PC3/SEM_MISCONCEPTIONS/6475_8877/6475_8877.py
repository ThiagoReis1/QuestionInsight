import math

# faça seu código aqui!
lado_apot = float(input("Digite um numero: "))

apot = lado_apot / (2 * math.tan(math.pi / 12))
area_dode = 6 * lado_apot * apot

print(float(round(area_dode,2)))