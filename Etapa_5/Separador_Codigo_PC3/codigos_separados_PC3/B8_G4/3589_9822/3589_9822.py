from numpy import*

v1 = array(eval(input()))

i = 0
soma = 0
while i <len (v1):
	if v1 [i] ==1:
		soma += 80
	elif v1 [i] == 2:
		soma += 40
	elif v1 [i] == 3:
		soma += 20
	elif v1 [i] == 4:
		soma += 10
	i += 1
print(soma)