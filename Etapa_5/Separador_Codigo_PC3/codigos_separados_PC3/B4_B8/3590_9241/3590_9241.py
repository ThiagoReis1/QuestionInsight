dado= eval(input("digite o numero de faces: "))

pontuacao_total=0

for i in range(len(dado)):
	
	if dado[i] == 1:
		pontuacao_total += 10
	elif dado[i] == 2:
		pontuacao_total += 5
	elif dado[i] == 3:
		pontuacao_total +=0
	elif dado[i] == 4:
		pontuacao_total += 5
	elif dado[i] == 5:
		pontuacao_total += 20
	elif dado[i] == 6:
		pontuacao_total +=10
		
print(pontuacao_total)


