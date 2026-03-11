from numpy import *
vet = array(eval(input("")))
i = 0
tt = 0
acc = 0
while i < size(vet):
	if vet[i] > 80:
		tt = vet[i] / 100 * 15
		acc = tt
	else:
		acc = acc + vet[i]
	i += 1
print(round(acc,2))