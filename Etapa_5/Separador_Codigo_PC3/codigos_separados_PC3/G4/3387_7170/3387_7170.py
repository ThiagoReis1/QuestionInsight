y = input("Qual a Unidade? Milhas por Galao (M) ou KM/L (K)? ").upper()
a = float(input("Qual o Valor da Medida?: "))

if y == "K":
	x = 2.35215*a
	print(round(x, 2))
	
else:
	x = a/2.35215
	print(round(x, 2))