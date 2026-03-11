from numpy import *
vet = array(eval(input("vetor de entrada: ")))
total = 0

for i in range(size(vet)):
	if(total < 55):
		total = vet[i] + total
		if(total >= 55):
			total = 0
print(total)