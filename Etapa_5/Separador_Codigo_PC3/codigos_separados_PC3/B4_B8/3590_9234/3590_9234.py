dados = eval(input("digite o vetor de dados acertados pelo jugaddor: "))
total = 0
for i in range(len(dados)):
	dado = dados[i]
	if dado == 1:
		total += 10
	elif dado == 2:
		total += 5
	elif dado == 3:
		total += 0
	elif dado == 4:
		total += 5
	elif dado == 5:
		total += 20
	elif dado == 6:
		total += 10
print(total)