from numpy import*

i = 0
soma = 200

a = array(eval(input()))

while i < size(a):
	if a[i]== 1:
		soma = soma/2
	elif a[i]== 2:
		soma = soma * 3
	elif a[i] == 3:
		soma = soma/2
	elif a[i] == 4:
		soma = soma *3
	elif a[i] == 5:
		soma = soma/2
	else:
		soma = soma * 3
	i = i + 1
print(round(soma,2))

