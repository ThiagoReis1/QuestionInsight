from numpy import*

x = input("").upper().split(",")
vet = zeros(4 ,dtype=int)


for i in range(size(x)):
	if (x[i]=="A"):
		vet[0] = vet[0]+1
	if (x[i]=="B"):
		vet[1] = vet[1]+1
	if (x[i]=="C"):
		vet[2]= vet[2]+1
	if (x[i]=="D"):
		vet[3] = vet[3]+1
print(vet)
		
		
		

	


