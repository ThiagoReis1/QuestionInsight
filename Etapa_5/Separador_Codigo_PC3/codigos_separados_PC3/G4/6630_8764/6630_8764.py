# faça seu código aqui!
from numpy import*

n = input("Digite aqui: ").upper()

cont = 0
i = 0

while i < len(n):
	if n[i] == "L":
		cont = cont + 1
		print(i)
	i = i + 1
if cont == 0:
	print ("nao achei")



