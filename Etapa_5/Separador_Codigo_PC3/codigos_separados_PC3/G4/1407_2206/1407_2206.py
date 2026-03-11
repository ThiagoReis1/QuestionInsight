from math import *
pv = int(input("quantidade inicial de pontos de vida: "))
v1 = int(input("valor de v1: "))
v2 = int(input("valor de v2: "))
v3 = int(input("valor de v3: "))
vl = v1 + v2 + v3
N = 10 * vl
pontos = pv - N
if(pontos > 0):
	print(pontos)
	print("VIVO")
else:
	print("0")
	print("MORTO")
	