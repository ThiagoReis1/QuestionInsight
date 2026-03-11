from numpy import*

vet = array(eval(input("")))

cont = 0 
desc = 5.00

for i in range(size(vet)):
	if(vet[i]>80.0):
		vet[i] = vet[i] - desc
		total = sum(vet)
print(total)
