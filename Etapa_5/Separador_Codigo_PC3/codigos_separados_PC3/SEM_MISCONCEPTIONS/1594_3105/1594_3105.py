from numpy import*
danos=array(eval(input()))
i=0
peso=0
acumulador=0

while (i<size(danos)):
	peso=peso+1
	acumulador=acumulador+danos[i]*peso
	i=i+1
print(acumulador)