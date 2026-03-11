#Varíaveis
r = float(input("raio: "))
n = int(input("lados: "))
#Cálculo
import math
a = r * math.cos(math.pi / n)
#Saída
print(round(a, 2))