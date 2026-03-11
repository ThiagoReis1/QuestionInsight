# faça seu código aqui!
from numpy import*
frase = input("Coloque sua frase: ").upper()

contador_e = 0
i = 0
while i < len(frase):
	if frase[i] == "L":
		contador_e += 1
		print(i)
	i += 1
if "L" not in frase:
	print("nao achei")

