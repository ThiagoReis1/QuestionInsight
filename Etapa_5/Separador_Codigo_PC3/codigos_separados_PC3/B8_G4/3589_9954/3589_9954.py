from numpy import*
a = array(eval(input()))
soma = 0
i = 0 
while i < size(a):
	if a[i] == 1:
		soma = soma + 80
	elif a[i] == 2:
		soma = soma + 40
	elif a[i] == 3:
		soma = soma + 20
	elif a[i] == 4:
		soma = soma + 10
	i = i + 1
print(round(soma,2))