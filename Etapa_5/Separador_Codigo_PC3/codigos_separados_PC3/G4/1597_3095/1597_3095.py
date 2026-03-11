from numpy import*
v = array(eval(input()))
i = 0
soma = 0
while(i < size(v)):
	if(float(v[i]) > 80):
		v[i] = v[i] - 5
	else:
		v[i] = v[i]
		soma = soma + float(v[i])
	i = i + 1
print(round(soma,2))
		