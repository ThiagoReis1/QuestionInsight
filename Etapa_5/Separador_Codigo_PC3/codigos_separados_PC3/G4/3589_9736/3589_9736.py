from numpy import *

a = array(eval(input()))
i = 0
soma = 0

while i < size(a):
	if a[i] == 1:
		soma = soma + 80
	elif a[i] == 2:
		soma = soma + 40
	elif a[i] == 3:
		soma = soma + 20
	else:
		soma = soma + 10
	i = i + 1
	
print(round(soma, 2))