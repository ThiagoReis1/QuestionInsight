from numpy import *

temperaturas = array(eval(input("temperaturas:")))

contador = 0
i = 0
while(i < size (temperaturas)):
	if(temperaturas[i] <= 0 or temperaturas >= 40):
		contador = contador + 1
	i = i + 1 
	
vet_v = array(zeros(contador, dtype = float))	
print(vet_v)