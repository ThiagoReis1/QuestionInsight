from numpy import*

somatorio = array(eval(input("")))

soma = 0

for i in range(size(somatorio)):
	
	if somatorio[i] == 88:
		soma = soma/2
	else:
		soma = soma + somatorio[i]

print(soma)