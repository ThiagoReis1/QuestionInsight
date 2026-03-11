from numpy import*

vet = array(eval(input("Valores:")))

cont = 0

for i in range(size(vet)):
	if(vet[i] >= 2000):
		cont = cont + 1

resultado = 0
j = zeros(cont,dtype=int)
for i in range(size(vet)):
	if(vet[i] >= 2000):
		j[resultado] = i	
		resultado = resultado + 1
print(cont)
print(j)