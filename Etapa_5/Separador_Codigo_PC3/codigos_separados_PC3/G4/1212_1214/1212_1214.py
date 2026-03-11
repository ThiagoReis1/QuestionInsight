#Universidade Federal do Amazonas
#Icomp
#Larissa Magno Leão-21551610
#Exercicio 1

from  numpy import*

p= array(eval(input("Informe os pesos levantados:")))

i= 0
cont= 0
r= 307
while(i < size(p)):
	if(p[i] < r):
		cont= cont+1
	i= i+1
print(r)
print(cont)