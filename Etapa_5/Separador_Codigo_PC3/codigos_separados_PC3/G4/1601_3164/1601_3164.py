from numpy import*

vet=array(eval(input("numeros:")))

m=min(vet)
i=0
for i in range(size(vet)):
	if vet[i]==m:
		print(i)
		
