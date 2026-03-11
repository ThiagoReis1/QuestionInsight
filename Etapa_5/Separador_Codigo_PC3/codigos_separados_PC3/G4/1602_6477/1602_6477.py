from numpy import*
vet = array(eval(input(":")))
i = 0

while i < size(vet) -1 :
	if (vet[i] == max(vet)):
		a = i
	i = i + 1
	
print(a)