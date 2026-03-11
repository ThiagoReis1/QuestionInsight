from numpy import*
palavra = input("").upper()
i = 0
soma = 0
while(i < len(palavra)):
	if(palavra[i] == "A"):
		soma = soma + 45.15
		i = i + 1
	elif(palavra[i] == "E"):
		soma = soma + 45.15
		i = i + 1
	elif(palavra[i] == "I"):
		soma = soma + 45.15
		i = i + 1
	elif(palavra[i] == "O"):
		soma = soma + 45.15
		i = i + 1
	elif(palavra[i] == "U"):
		soma = soma + 45.15
		i = i + 1
	else:
		soma = soma + 50.17
		i = i + 1
print(round(soma, 2))