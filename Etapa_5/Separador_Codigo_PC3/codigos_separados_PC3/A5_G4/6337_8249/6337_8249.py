import numpy 

vet = array(eval(input()))

n = int(input())
i = 0
contR = 0

while i < size(vet):
	if (vet[i]) == n:
		print(i)
	if (vet[i]) < n:
		contR = contR + 1
	i = i + 1
print(contR)
	