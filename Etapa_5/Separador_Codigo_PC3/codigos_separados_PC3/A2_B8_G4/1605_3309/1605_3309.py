from numpy import*
vet = array(eval(input("vetor: ")))
a = 200
i = 0

while (i < size(vet)):
	if (vet[i] == 1):
		a = a*4
	elif (vet[i] == 2):
		a = a*2
	elif (vet[i] == 3):
		a = a
	elif (vet[i] == 4):
		a = a/2
	i = i + 1
print(round(a, 2))