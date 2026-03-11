string = input().upper()

iogurt = 3.75
massas = 4.50
salgadinhos = 2.90

i = 0 
soma = 0  
while i < len(string):
	if string[i] == "I":
		soma = soma + iogurt
	elif string[i] == "M":
		soma = soma + massas 
	elif string[i] == "S":
		soma = soma + salgadinhos
	i = i + 1
	
print(round(soma, 2))
	
	
	