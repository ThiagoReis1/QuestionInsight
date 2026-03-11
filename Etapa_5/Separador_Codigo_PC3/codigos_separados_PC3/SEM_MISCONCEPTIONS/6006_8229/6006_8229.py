numero_batatas = int(input("Digite o numero de batatas compradas: "))

if numero_batatas <10:
	valor_total = numero_batatas * 0.90
else:
	valor_total = numero_batatas * 0.75
print(round(valor_total, 2))