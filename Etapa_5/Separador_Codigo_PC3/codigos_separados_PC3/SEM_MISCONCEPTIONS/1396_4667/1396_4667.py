valor_consumido=float(input())

if (valor_consumido <= 300.00):
	gorjeta=(0.1*valor_consumido)
	valor_total=gorjeta+valor_consumido
else:
	(valor_consumido >= 300.00)
	gorjeta=(0.06*valor_consumido)
	valor_total=gorjeta+valor_consumido

print(round(valor_total,2))	