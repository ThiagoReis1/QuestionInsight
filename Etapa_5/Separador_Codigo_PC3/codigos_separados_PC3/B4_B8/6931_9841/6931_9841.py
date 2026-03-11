valor = float(input())
codigo = str(input()).upper()
if codigo == "D":
	desconto = valor - valor*(18/100)
elif codigo == "P":
	desconto = valor - valor*(18/100)
elif codigo == "C":
	parcela = int(input())
	if parcela == 1:
		desconto = valor
	else:
		desconto = valor + valor*(7/100)
print(round(desconto,2))