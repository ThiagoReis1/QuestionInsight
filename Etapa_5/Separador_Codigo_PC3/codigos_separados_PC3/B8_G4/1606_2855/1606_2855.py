from numpy import*

vet = array(eval(input("andares")))

total = 0
i = 0
j = 1

while(j < size(vet)):
	if(vet[i] > vet[j]):
		total = total + vet[i] - vet[j]
	elif(vet[i] < vet[j]):
		total = total + vet[j] - vet[i]
	i = i + 1
	j = j + 1
	
print(total)
		