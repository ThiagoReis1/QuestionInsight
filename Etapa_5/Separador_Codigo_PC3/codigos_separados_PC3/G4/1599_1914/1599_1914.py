from numpy import*
v = array(eval(input("")))
i = 0
soma = 0.0
while(i<size(v)):
	if(v[i]>80):
		soma = soma + 0.85*v[i]
	else:
		soma = soma + v[i]
	i = i + 1
print(round(soma,2))