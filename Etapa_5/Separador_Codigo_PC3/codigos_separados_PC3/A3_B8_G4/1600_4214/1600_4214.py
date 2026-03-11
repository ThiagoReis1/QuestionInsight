from numpy import *
vet=array(eval(input("Custo dos itens:")))
i=0
j=size(vet)
valor= 0
while(j<sum(vet)):
	if(vet[i]<=80 and vet[i]>0):
		valor= sum(vet)
		j=j+1
	elif(vet[i] > 80):
		desc= vet* (15/100)
		valor= valor + desc
		j=j+1
print(round(valor,2))