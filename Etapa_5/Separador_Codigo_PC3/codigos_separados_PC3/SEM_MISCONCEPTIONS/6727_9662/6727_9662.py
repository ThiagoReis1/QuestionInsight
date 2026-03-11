numero = int(input("Digite um numero inteiro:"))
if numero%31==0:
	print(numero//31)
	print("sim")
else:
	print(numero%31)
	print("nao")