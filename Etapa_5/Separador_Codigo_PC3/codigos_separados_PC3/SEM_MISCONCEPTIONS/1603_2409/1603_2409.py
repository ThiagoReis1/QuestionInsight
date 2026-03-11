from numpy import *
numeros = array(eval(input("numeros: ")))
i = 0
anel = 0
while(i < size(numeros)):
	if(numeros[i] == 1):
		anel = anel + 80
	if(numeros[i] == 2):
		anel = anel + 40
	if(numeros[i] == 3):
		anel = anel + 20
	i = i + 1
print(anel)