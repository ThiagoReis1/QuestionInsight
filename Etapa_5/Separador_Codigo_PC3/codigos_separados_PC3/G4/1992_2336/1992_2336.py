aminoacido = input("digite o aminoacido: ")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

if aminoacido == "Glutamina":
	X = C*5 + H*8 + N*1 + O*4
	print(round(X,2))
elif aminoacido == "Histidina":
	X = C*6 + H*10 + N*3 + O*2
	print(round(X,2))
elif aminoacido == "Prolina":
	X = C*5 + H*10 + N + O*2
	print(round(X,2))
else:
	print("Entrada:",aminoacido)
	print("Dados Invalidos")