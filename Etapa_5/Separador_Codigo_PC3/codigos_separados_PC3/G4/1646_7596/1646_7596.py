from numpy import *
vet = array(eval(input("saques: ")))
cont = 0
j = 0


for i in range(size(vet)):
	if (vet[i] <= 50):
		cont = cont + 1
resultado = zeros(cont, dtype = int)
for i in range(size(vet)):
	if (vet[i] <= 50):
		resultado[j] = i
		j = j + 1

print(cont)
print(resultado)