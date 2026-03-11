from numpy import*

x = array(eval(input()))

soma = 0
notas = 0

for i in range(size(x)):
	if(x[i] == 88):
		soma = soma / 2
	else:
		soma = soma + x[i]
		
print(soma)
	