from numpy import*
v = array(eval(input("Digite:")))
cont = 0
soma = 0
sum(v) 
while(cont<size(v)):
	if(v[cont]>80):
		v[cont] = v[cont] - 1
	else:		
		soma = v[cont]
	cont = cont + 1
print(round(soma,2))