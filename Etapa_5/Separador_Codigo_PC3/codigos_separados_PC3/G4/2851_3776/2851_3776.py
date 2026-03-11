from numpy import *
c= array(eval(input()))
i=0
soma=0
while(i < size(c)):
	if(i>=0):
		soma=soma+c[i]
		i=i+1
	if(c[i-1] == 99):
		soma=soma*2-2*99
print(soma)
		