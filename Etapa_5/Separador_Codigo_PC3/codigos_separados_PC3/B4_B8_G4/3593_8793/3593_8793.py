from numpy import *
n = array(eval(input('digite os valores do vetor:')))
soma = 200
i = 0

while i < size(n):
	if n [i] == 1 :
		soma = soma / 2
	elif n [i] == 2 :
		soma = soma * 3
	elif n [i] == 3:
		soma = soma / 2
	elif n [i] == 4:
		soma = soma * 3
	elif n [i] == 5:
		soma = soma / 2
	elif n [i] == 6 :
		soma = soma * 3
	i += 1
print(round(soma, 2))
	
