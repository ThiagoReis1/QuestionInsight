from numpy import*
vet = array(eval(input("Digite as temperaturas:")))
i=0
j=0
vinv = 0

while (i<size(vet)):
	if (vet[i] > -100):
		vinv = vinv + 1
	i = i+1
i=0
vet2 = array(ones(vinv,dtype=float))
while (i<size(vet)):
	if (vet[i] > -100):
		vet2[j] = vet[i]
		j = j+1
	i = i+1
print (vet2)