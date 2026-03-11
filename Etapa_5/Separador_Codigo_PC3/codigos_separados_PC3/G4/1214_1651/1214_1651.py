from numpy import *
vet=array(eval(input("Quais os pesos de levantamento?")))
recorde=217
i=0
j=0
while(i<size(vet)):
	if(vet [i]<(recorde)):
		j=j+1
	i=i+1
print(recorde)
print(j)
