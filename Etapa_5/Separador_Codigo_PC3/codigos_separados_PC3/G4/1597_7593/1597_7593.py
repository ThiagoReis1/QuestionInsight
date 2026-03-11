from numpy import*

vet = array(eval(input("compra: ")))

for i in range(size(vet)):
	if(vet[i]>80):
		vet[i] = vet[i] - 5
print(round(sum(vet), 2))