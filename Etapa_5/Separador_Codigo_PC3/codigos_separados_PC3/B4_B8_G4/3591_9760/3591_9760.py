from numpy import*

a = array(eval(input()))
i = 0
soma = 0

while i < size(a):
	if a[i] == 1:
		soma = soma + 10
	elif a[i] == 2:
		soma = soma + 5
	elif a[i] == 3:
		soma = soma + 10
	elif a [i] == 4:
		soma = soma + 5
	elif a[i] == 5:
		soma = soma + 10
	elif a[i] == 6:
		soma = soma + 5
	i = i + 1
print(soma)