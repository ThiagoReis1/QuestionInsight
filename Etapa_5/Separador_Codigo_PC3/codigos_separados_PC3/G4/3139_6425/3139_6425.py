from numpy import *
vetor=array(eval(input("numeros reais positivos: ")))
i=0
acum=0
while (i < size(vetor)):
	acum=acum +(vetor[i]**(1/3))
	i+=1
	
m=(acum/size(vetor)) **3
print(round(m,2))
	
	