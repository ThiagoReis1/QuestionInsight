from numpy import*
vet = array(eval(input("numeros: ")))
cont1 = 0
for i in range(size(vet)):
	if(vet[i]>=70):
		cont1 = cont1 + 1
i =0 
cont2 = 0
vet2 = zeros(cont1,dtype=int)
for i in range(size(vet)):
	if(vet[i]>=70):
		vet2[cont2] = i
		cont2 =cont2 + 1
print(cont1)
print(vet2)