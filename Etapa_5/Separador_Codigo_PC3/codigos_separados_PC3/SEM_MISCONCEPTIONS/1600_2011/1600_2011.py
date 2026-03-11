from numpy import *
custo = array(eval(input("  ")))
i=0
soma=0
soma2=0
while(i <	size(custo)):
	if(custo[i] > 80.0):
		soma=soma+custo[i]*0,85
		print(soma)
		i=i+1
		
	else:
		soma2=soma2 + custo[i] 
		i=i+1
		
print(soma2 + soma)