from numpy import*
vet = array(eval(input()))
i=0

a = zeros(size(vet),dtype = int)
for i in range(size(vet)):
	if vet[i] !=9:
		a[i] = vet[i] + 1
	else:
		a[i] = 0	
print(a)
	
	

