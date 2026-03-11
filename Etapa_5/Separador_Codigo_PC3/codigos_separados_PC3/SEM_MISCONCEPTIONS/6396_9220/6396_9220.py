from numpy import *

vet = array(eval(input("numeros a serem subtituidos: ")))
new_vet = zeros(size(vet), dtype = int)

for i in range(size(vet)):
	if vet[i] == 7:
		new_vet[i] == 14
	else:
		new_vet[i] = 2 * vet[i]

print(new_vet)