from numpy import * 

vet = array(eval(input()))

a = zeros(size(vet), dtype = int)

for i in range(size(vet)):
	if(vet[i] != 0):
		a[i] = vet[i] - 1
	else:
		a[i] = 9
print(a)

		
	