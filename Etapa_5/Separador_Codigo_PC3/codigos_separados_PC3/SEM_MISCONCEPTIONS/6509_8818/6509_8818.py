# faça seu código aqui!
hora = float(input("digite o horario"))
qtde =int(input("digite quantidade"))

total = qtde*28.50

if hora >= 18:
	desconto = (20/100)*total
	valor_pago = total-desconto
	print(round(valor_pago,2))
else:
   print(round(total, 2))
