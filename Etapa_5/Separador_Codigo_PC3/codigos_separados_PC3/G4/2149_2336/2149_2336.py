from numpy import*
vet1 = array(eval(input()))
vet2 = array(eval(input()))

vet = vet1 + vet2
print(vet)
x = 0
for i in range(size(vet)):
	if vet[i] >= 12:
		x += 1
print(x)
		