# faça seu código aqui!

dia = int(input("qt de dias reservados:"))

taxa = 175

if dia < 15:
	valor = dia * taxa + 20
	print(round(valor,2))
elif dia == 15:
	valor = dia * taxa + 16
	print(round(valor,2))
else:
	valor = dia * taxa + 10
	print(round(valor,2))