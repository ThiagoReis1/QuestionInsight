from numpy import *

vet = array(eval(input()))

rep = 0
for i in vet:
	if(i < 5):
		rep = rep + 1
print(rep)

#reprovados = zeros(rep,dtype = int)

x = 0
for i in vet:
	if(i < 5):
		x = x + vet[i]
print(x)