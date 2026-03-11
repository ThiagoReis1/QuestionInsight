from numpy import *
v = array(eval(input("vetor de passageiros:")))

i = 0
soma = 0

while(i<size(v)):
	soma = soma + v[i]
	i = i + 1
	
print(soma)