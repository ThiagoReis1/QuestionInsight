from numpy import *

categoria = zeros(4, dtype=int)
produto = input("Insira o pruduto (E) eletronicos (V) vestuario (A) alimentos (D) decoracao: ").upper().split(",")

for v in produto:
	if v == "E":
		categoria[0] += 1
	elif v == "V":
		categoria[1] += 1
	elif v == "A":
		categoria[2] += 1
	elif v == "D":
		categoria[3] += 1
		
print(categoria)
