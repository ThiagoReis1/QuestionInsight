
volume = float(input("Insira o valor:"))
taxa  = 30

if (volume <10):
	valor = taxa + volume*3.0
	print(round(valor,2))

else:
	valor = taxa + volume*3.5
	print(round(valor,2))