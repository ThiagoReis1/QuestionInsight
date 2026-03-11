from numpy import *

notas = array(eval(input()))
pesos = [3,2,4,1,3]
soma= 0
i=0
while(i<len(notas)):
	soma+= notas[i]*pesos[i]
	i+=1
print(round(soma/sum(pesos),2))