qttd = int(input("Digite a quantidade de milho:\n"))

if qttd < 6:
	custo = 1.85
else:
	custo = 1.50
	
valor = qttd * custo

print(round(valor, 2))