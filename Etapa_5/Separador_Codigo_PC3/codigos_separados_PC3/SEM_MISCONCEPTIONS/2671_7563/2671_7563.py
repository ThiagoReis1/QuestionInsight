import math 

r = float(input("Raio: "))
n = int(input("Numero do poligono: "))

apotema = r * (math.cos(math.pi / n )) 

print(round(apotema, 2))
					