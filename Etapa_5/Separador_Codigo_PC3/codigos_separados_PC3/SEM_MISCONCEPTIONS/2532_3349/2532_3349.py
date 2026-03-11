C = float(input("Insira o valor do carro: "))
D = float(input("Insira o valor inicial depositado: "))
M = float(input("Insira o deposito mensal fixo: "))
j = float(input("Insira a taxa de juros: "))
tempo_mes = 0
lucro = D
if(C > 0 and D > 0 and M > 0 and j > 0):
	while (lucro < C):
		lucro = lucro+lucro * (j/100) +M
		lucro=round(lucro,2)
		tempo_mes = tempo_mes + 1
	print(tempo_mes)
else:
	print("Dados incorretos")