from numpy import* 
v = array(eval(input()))
i = 0

soma = 0
while(i < size(v)):
	if(v[i]>0):
		soma = soma + v[i]
	else:
		soma = soma - v[i]
	i = i + 1
print(soma)