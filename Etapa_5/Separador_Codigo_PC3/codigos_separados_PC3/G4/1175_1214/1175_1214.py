#Universidade Federal do Amazonas
#Icomp
#Larissa Magno Leão-21551610
#Exercicio 2
from math import*

n= int(input("Informe n:"))

i= 1
sinal= -1
soma= 0
d= 9

while(i<= n):
	
	soma= soma + sinal*sqrt(i)/d
	
	i= i+1
	sinal= -sinal
	d= d+2
	
print(round(soma,5))