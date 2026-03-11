from numpy import*
vet = input("Digite: ").upper()
i = 0
a = 0
while(i < len(vet)):
	if(vet[i] == "C"):
		a = a + 1
	i = i + 1
print(a)
		


