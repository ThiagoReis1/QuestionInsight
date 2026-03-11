valor = float(input("Volume de vendas:"))
if (valor>1000):
	valor = 50+(valor-1000)*0.1
	print(round(valor,2))
else:
	valor = valor*0.05
	print(round(valor,2))