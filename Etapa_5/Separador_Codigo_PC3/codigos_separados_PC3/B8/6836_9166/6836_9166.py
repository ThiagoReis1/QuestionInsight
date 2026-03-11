produto = input().upper()

i, soma = 0, 0
while (i < len(produto)):
	if (produto[i] == "B"):
		soma = soma + 6.80
	elif (produto[i] == "C"):
		soma = soma + 11.75
	elif (produto[i] == "M"):
		soma = soma + 5.90
	i = i + 1
	
print(round(soma, 2))