from numpy import *
notas = array(eval(input("notas: ")))
peso= [1, 3, 2, 5]
i=0
n=0

while i < size(notas):
   n= n + notas[i] * peso[i]
   i= i +1	
	
print(round(n/sum(peso),2))
