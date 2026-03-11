from numpy import*

vet = array(eval(input("Vetores: ")))

cont = zeros(2,dtype=int)

for i in range(size(vet)):
	if vet[i] <= 50:
		cont[0] = con[0] + 1
print(max(vet))