from numpy import*

vet = array(eval(input("insira os valores: ")))
cont = 0

for i in range(size(vet)):
	if (vet[i] % 3 == 0):
		cont = cont + 1

cont1 = zeros(cont,dtype=int)
cont = 0
for i in range(size(vet)):
	if (vet[i] % 3 == 0):
		cont1[cont] = i 
		cont = cont + 1
		
print(cont)
print(cont1)