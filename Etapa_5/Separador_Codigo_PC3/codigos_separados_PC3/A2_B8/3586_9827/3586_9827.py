from numpy import*

vet = array(eval(input()))
i=0
total=0
while	i < size(vet):
	if	vet[i] == 1:
		total += 100
	elif	vet[i] == 2:
		total += 60
	elif	vet[i] == 3:
		total += 20
	elif	vet[i] == 4:
		total = total
	i += 1
print(round(total,2))