masa= float(input("quantidade de maçãs compradas: "))
unidade= 0.30
desconto= 0.25
desconto_duzia= 12
if masa < desconto_duzia:
	valor_total= masa * unidade*
else:
	valor_total= masa * desconto
	return valor_total

print(round(valor_total, 2))
