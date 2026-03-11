from numpy import*

a = array(eval(input("")))
i = 0
soma = 200

while i < len(a):
	if a[i] == 1:
		soma = soma/2
	elif a[i] == 2:
		soma = soma*3
	elif a[i] == 3:
		soma = soma/2
	elif a[i] == 4:
		soma = soma*3
	elif a[i] == 5:
		soma = soma/2
	elif a[i] == 6:
		soma = soma*3
	i = i + 1
print(round(soma, 2))