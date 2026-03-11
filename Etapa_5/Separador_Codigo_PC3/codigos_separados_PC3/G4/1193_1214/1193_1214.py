#Universidade Federal do Amazonas
#Icomp
#Larissa Magno Leão-21551610
#Exercicio 2

from numpy import*

t= array(eval(input("Informe as temperaturas:")))

i= 0
cont= 0

while(i < size(t)):
	if(t[i] > -100):
		cont= cont+1
	i= i+1
	
n= array(zeros(cont,dtype=float))

i= 0
j= 0

while(i < size(t)):
	if(t[i] > -100):
		n[j]= t[i]
		j= j+1
	i= i+1

print(n)