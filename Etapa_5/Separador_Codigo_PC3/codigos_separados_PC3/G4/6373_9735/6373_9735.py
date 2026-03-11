from numpy import*
a = input("").upper().split(",")
vet = zeros(4, dtype=int)
for i in range(size(a)):
	if a[i] == "A":
		vet[0] = vet[0] + 1
	if a[i] == "P":
		vet[1] = vet[1] + 1
	if a[i] == "D":
		vet[2] = vet[2] + 1
	if a[i] == "M":
		vet[3] = vet[3] + 1
print(vet)
		