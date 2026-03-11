valor_consumido = float(input("Valor consumido: "))
vc = valor_consumido
if vc > 300:
	valor_pago = round(float(vc + (vc *0.06)),2)
	print(valor_pago)
else:
	valor_pago = round(float(vc + (vc *0.1)),2)
	print(valor_pago)