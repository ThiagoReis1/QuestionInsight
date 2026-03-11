compra1 = float(input('valor1 : \n'))
compra2 = float(input('valor2 : \n'))
compra3 = float(input('valor3 : \n'))
limite = float(input(' informe o limite do cartão: \n'))
valorTotal = compra1 + compra2 + compra3 
print(valorTotal)
if valorTotal <= limite:
	print ('Sim')
else:
	print ('Nao')
