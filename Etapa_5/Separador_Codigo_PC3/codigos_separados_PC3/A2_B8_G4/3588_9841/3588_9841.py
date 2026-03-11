from numpy import array
n = array(eval(input()))
soma = 10000
for c in range(0,len(n)):
	if n[c] == 1:
		soma = soma*2
	elif n[c] == 2:
		soma = soma 
	elif n[c] == 3:
		soma = soma/2
	elif n[c] == 4:
		soma = soma/4
print(round(soma,2))