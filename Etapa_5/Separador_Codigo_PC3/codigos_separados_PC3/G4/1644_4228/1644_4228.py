from numpy import*
vet = array(eval(input("Nota: ")))
i = zeros(1, dtype=int)

for i in range(size(vet)):
	if (vet[i] <= 5):
		print(i)
		
for i in range(size(vet)):
	if (vet[i] <= 5):
		print([i])