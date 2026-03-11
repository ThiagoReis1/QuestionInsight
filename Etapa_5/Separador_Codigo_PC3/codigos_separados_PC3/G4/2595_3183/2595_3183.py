from numpy import*
vet = array(eval(input("servicos ")))
a = 0
for i in range(size(vet)):
	if(vet[i] == vet[0] or vet[i] < vet[0]):
		a = a + 1
		print(size(vet[i]))
		
print(size(vet[i]))
print(a)