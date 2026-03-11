from numpy import *

entrada = array(eval(input()))

i=0
soma =0
while(i<len(entrada)):
	if(entrada[i]%2==0):
		soma+=5
	else:
		soma+=10
	i+=1
print(soma)