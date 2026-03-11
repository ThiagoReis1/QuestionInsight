from numpy import*
i=0
levM=0
rec = 217
vet = array(eval(input("Digite os pesos do levantamento:")))
print (rec)
while (i<size(vet)):
	if (vet[i]<217 and vet[i] >= 0):
		levM = levM+1
	i = i+1
print(levM)