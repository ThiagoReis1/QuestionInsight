from numpy import*

x = array(eval(input()))
soma = 0
for i in range(size(x)):
	if x[i] != 0:
		soma += x[i]
	else:
		soma = 0 
print(soma)