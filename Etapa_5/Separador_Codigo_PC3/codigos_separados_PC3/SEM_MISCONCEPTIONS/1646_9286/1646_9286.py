from numpy import *
saques = array(eval(input("Saques:")))
cont = 0
for i in range(size(saques)):
	if saques[i] <=50:
		cont+=1
print(cont)

valor =  zeros(cont, dtype=int)
j=0
for i in range (size(saques)):
	if saques[i] <=50:
		valor[j] = i
		j+=1
		
print(valor)