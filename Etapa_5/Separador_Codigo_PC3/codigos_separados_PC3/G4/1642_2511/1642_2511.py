from numpy import*
vet1 = array(eval(input("Primeiro vetor: ")))
k =0
cont = 0
for elementos in vet1:
	if (elementos % 5 == 0): 
		cont = cont + 1
print (cont)

cont1 = zeros(5,dtype=int)
for i in range(size(vet1)):
	if (vet1[i] % 5 == 0):
		cont1[k] = i
print (vet1)