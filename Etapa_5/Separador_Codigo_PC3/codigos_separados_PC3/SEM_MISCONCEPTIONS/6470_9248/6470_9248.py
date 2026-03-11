import math

# faça seu código aqui!
lado = float(input("lado do heptagono: "))
				 
divisor = 2 * math.tan(math.pi / 7)
apotema = lado / divisor
				 
area = (7 * lado * apotema) / 2

print(round(area, 2))