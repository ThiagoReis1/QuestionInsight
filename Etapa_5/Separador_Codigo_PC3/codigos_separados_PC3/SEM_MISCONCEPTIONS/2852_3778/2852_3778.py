from numpy import*
vetor = array(eval(input()))
soma = 0
for i in vetor:
	if i != 88:
		soma = soma + i
	else:
		soma = soma / 2
print(soma)