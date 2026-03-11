# faça seu código aqui!
tempo = float(input('horario que sera feito o pedido no restaurante: '))
qtde = float(input('quantidade de pratos pedidos: '))

if tempo >= 18:
	a = 28.50 * qtde
	valor = a * 0.20
	valor_total = a - valor
	print(round(valor_total , 2))
else:	
	a = 28.50 * qtde 
	valor_total = a
	print(round(valor_total , 2))
 