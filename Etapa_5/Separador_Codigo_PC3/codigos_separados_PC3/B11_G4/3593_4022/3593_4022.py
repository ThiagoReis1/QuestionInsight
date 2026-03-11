from numpy import *

vet = array(eval(input("face do dado: ")))

i = 0 
c = 200

while i<size(vet):
	if vet[i] == 1:
		c = c/2

	if vet[i] == 2:
		c = c*3

	if vet[i] == 3:
		c = c/2

	if vet[i] == 4:
		c = c*3
	
	if vet[i] == 5:
		c = c/2

	if vet[i] == 6:
		c = c*3
	i+=1

print(round(c, 2))