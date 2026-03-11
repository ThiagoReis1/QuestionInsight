from numpy import *
v=array(eval(input("Digite os pesos: ")))
cont=0
i=0
recorde=307
while(i<size(v)):
	if(v[i]>recorde):
		cont=cont+1
	i=i+1	
print(recorde)
print(cont)