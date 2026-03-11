from numpy import*
v= array(eval(input("")))
i=0
soma= 0

while i < size(v):
	if v[i] == 1:
		soma= soma + 10
	elif v[i] == 2:
		soma= soma + 5
	elif v[i] == 3:
		soma = soma + 0
	elif v[i] == 4:
		soma = soma + 5
	elif v[i] == 5:
		soma= soma + 20
	elif v[i] == 6:
		soma= soma + 10
	i = i + 1
print(soma)