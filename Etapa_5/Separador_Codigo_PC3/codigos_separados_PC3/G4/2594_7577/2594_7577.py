from numpy import*

vet = array(eval(input("Entrada: ")))

cont = 0 
for i in range(1,size(vet)):
	if(vet[i] > vet[0]):
		print(i)
		cont = cont + 1 
print(cont)