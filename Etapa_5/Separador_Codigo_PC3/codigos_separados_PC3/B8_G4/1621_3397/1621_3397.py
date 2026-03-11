from numpy import*
prod = input("Digite o produto: ").upper()
qt = input("Digite a quantidade do produto: ")
i = 0

while(i < size(prod)):
	if('arroz' == prod[i]):
		soma = soma + (qt[i] * 1.25)
	elif ('feijao' == prod[i]):
		soma = soma + (qt[i] * 2.60)
	elif ('bis' == prod[i]):
		soma = soma + (qt[i] * 1.80)
	elif ('miojo' == prod[i]):
		soma = soma + (qt[i] * 0.85)
	elif ('fanta' == prod[i]):
		soma = soma + (qt[i] * 3.20)
	i = i + 1
	
print(round(soma, 2))
		