from numpy import*
c = array(eval(input()))
i=0
soma = 0
while (i < size(c)):
	if (i >= 0):
		soma= soma + c[i]
		i =i+1
	if(soma > 55):
		soma = 0
	
print(soma)
	