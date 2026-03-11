# faça seu código aqui!
from numpy import *

v = input("Selecione uma frase : ").upper()
i = 0
p = 0
while i < len(v):
	if v[i] == "P":
		p = p + 1
		print(i)
	i = i + 1
if (p == 0):
	print("nao achei")