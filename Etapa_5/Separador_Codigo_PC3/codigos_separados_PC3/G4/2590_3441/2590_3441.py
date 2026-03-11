from numpy import*
vet = array(eval(input()))
i1 = 0 #VARIAVEL CONTADORA
for x in range(1, size(vet)):
	if vet[x] < vet[0]:
		i1 += 1
		print(x)
print(i1)
		
