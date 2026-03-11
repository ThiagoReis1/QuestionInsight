mac = int(input("Digite o numero de ms"))
if mac<12:
	valor = mac * 0.30
	print(round(valor,2))
else:
	valor = mac * 0.25
	print(round(valor,2))