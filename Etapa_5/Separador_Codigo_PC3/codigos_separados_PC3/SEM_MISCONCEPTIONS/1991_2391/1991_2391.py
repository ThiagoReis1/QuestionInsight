aminoacido = input("Nome do aminoacido: ").upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

Glicina = C*2 + H*5 + N + O*2
Prolina = C*5 + H*10 + N + O*2
Serina = C*3 + H*7 + N + O*3

if (aminoacido == "GLICINA"):
	print(round(Glicina,2))
elif (aminoacido == "PROLINA"):
	print(round(Prolina,2))
elif (aminoacido == "SERINA"):
	print(round(Serina,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
