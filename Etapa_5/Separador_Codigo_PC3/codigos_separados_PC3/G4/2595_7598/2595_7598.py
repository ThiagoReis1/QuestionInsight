from numpy import*

vet = array(eval(input()))
i = 0
tx = 0


for i in range(size(vet)):
	if(vet[i] < 0 ) and (vet[i]<=vet[0]):
		print(i)
		tx = tx + 1

		
print(tx)