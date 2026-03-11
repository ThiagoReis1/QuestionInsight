from numpy import*

a = array(eval(input("")))
vet = zeros(size(a), dtype=int)
for i in range(size(a)):
#	if a[i] == "7":
	vet[i] = a[i]
	vet[i] = vet[i]**2
print(vet)
	