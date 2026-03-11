from numpy import * 

vet1 = array(eval(input("Notas:")))

total = 0 

for i in range(size(vet1)):
	if (vet1[i] == 10):
		total = total * 10
	else: 
		total = total + vet1[i]
		
print(total)