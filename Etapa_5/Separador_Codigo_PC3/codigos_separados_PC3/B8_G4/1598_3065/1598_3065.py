from numpy import*

vet = array(eval(input("vetor de compras : ")))

i = 0

while(i < size(vet)):
	if(vet[i] >= 80):
		vet[i]=vet[i]-5
		i=i+1
	elif(vet[i] < 80):
		i=i+1
print(round(sum(vet),2))