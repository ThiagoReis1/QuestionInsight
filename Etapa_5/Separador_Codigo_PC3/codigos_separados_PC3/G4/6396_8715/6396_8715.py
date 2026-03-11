from numpy import*

vet1 = array(eval(input()))
vet2 = zeros(size(vet1), dtype = int)

for i in range(size(vet1)):
	if vet1[i] == "0":
		vet2[i] = 0
	else:
		vet2[i] = vet1[i]*2
		
print(vet2)
	