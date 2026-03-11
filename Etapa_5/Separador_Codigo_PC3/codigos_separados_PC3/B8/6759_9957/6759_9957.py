# faça seu código aqui!
distancia = int(input())

custo_inicial = 50

#taxas adicionais
taxa_menorque10 = 5.50
taxa_igual10 = 7.75
taxa_maior10 = 10.00

#condicionais e calculo
if distancia < 10:
	resultado = taxa_menorque10 + custo_inicial
elif distancia == 10:
	resultado = custo_inicial + taxa_igual10
elif distancia > 10:
	resultado = custo_inicial + taxa_maior10
	
resultado_round = round(resultado, 2)
print(resultado_round)
	

