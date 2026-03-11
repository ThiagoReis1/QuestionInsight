valor_consumido = float(input("Digite o valor consumido: "))
if(valor_consumido <= 300):
	
	gorjeta = ((10/100)* valor_consumido)
	vt = gorjeta + valor_consumido
	print(round(vt,2))
	
elif(valor_consumido > 300):
	
	gorjeta_2 = ((6/100)*valor_consumido)
	vt2 = gorjeta_2 + valor_consumido
	print(round(vt2,2))
	
