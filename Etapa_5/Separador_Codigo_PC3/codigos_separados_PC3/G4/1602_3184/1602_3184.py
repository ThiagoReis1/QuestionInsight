from numpy import*
vet = array(eval(input("")))
i = 0

while(i<size(vet)):
	if(vet[i]!=max(vet)):
		i = i + 1
	else:
		print(i)
		i = i + 1