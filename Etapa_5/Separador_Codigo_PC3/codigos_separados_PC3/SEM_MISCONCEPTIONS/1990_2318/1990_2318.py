aminoacido = input("digite o aminoacido")

O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if aminoacido == "Glutamina":
	X = C*5 + H*8 + N*1 + O*4
	print(round(X,2))
elif aminoacido == "Serina":
	X = C*3 + H*7 + N + O*3
	print(round(X,2))
elif aminoacido == "Treonina":
	X = C*4 + H*9 + N + O*3
	print(round(X,2))
	else:
		print("Entrada:", aminoacido)
		print("Dados Invalidos")
