from numpy import*

vet = array(eval(input()))

a = 0

for i in range(size(vet)):
	if vet[i] < vet[0]:
		print(i)
		a = a + 1
print(a)
		