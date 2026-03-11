aneis = eval(input("anel acertado: "))
pontuacao_total = 10000

for y in range(len(aneis)):
	if aneis[y] == '1':
		pontuacao_total * 2
	elif aneis[y] == '2':
		pontuacao_total *1 
	elif aneis[y] == '3':
		pontuacao_total  / 2
	elif aneis[y] == '4':
		pontuacao_total / 4
				
pontuacao_total = round(pontuacao_total, 2)
print(pontuacao_total)