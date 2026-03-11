from numpy import*
v = array(eval(input("")))

i = 0
soma = 0
while i < size(v):
	if v[i] == 1:
		soma = soma + 80
	elif v[i] == 2:
		soma = soma + 40
	elif v[i] == 3:
		soma = soma + 20
	elif v[i] == 4:
		soma = soma + 10
	i = i + 1
	
print(soma)
		