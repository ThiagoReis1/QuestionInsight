from math import * 
raio = float(input("raio: "))
nl = int(input("lados: "))
lados = 2*raio*sin(pi/nl)
print(round(lados, 2))
