from numpy import *

recorde = 98.48
i = 0
abaixo = 0

vet1 = array(eval(input("digite os vetores: ")))

while(i<size(vet1)):
	if(vet1[i]>recorde):
		abaixo = abaixo + 1
	i = i + 1

print(recorde)	
print(abaixo)
