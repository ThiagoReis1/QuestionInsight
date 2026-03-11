valor_carro = float(input())
inicial_D = float(input())
deposito_M = float(input())
taxa_J = float(input())


if(valor_carro < 0 or inicial_D < 0 or deposito_M < 0 or taxa_J < 0):
	print("Dados incorretos")
else:
	valor_tem = inicial_D
	meses = 0
	juros = 0
	while(valor_tem < valor_carro):
		round(valor_tem, 2)
		juros =  ((valor_tem * taxa_J) / 100)
		valor_tem =  (valor_tem + juros + deposito_M)
		meses = meses + 1
		
	print(meses)
		
		
	
