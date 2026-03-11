from numpy import*

soma = 0

v = array(eval(input('escreva um vetor de numeros:')))

for i in v:
	if i != 99:
		soma += i
	else:
		soma = soma * 2
		
print(soma)

