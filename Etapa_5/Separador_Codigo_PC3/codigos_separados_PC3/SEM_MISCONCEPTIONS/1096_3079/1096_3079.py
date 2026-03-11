tempo_voo = float(input())


if(tempo_voo >= 200):
	calculo_valor = 10000 + (tempo_voo * 90)
	print(round(calculo_valor,2))
	
else:
	calculo_unidade = 5000 + (tempo_voo * 100)
	print(round(calculo_unidade,2))