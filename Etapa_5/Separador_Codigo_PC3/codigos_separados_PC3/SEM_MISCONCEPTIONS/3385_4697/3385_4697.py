unidade = input("Unidade: ")
valor = float(input("valor da medida: "))
A = valor/2.47105
H = valor*2.47105
if (unidade == H):
	print(round(A, 2))
else:
	print(round(H, 2))