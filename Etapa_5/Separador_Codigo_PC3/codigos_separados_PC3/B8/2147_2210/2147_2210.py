from numpy import*

senha=input("CPF: ")

if(senha%11):
	print("INVALIDO")
	
for i in range (1,range(senha),2):
	if(i==senha):
		vet[0]=vet[0]+1
	elif(i==senha):
		vet[1]=vet[1]+2
	elif(i==senha):
		vet[2]=vet[2]+3
	elif(i==senha):
		vet[3]=vet[3]+4
	elif(i==senha):
		vet[4]=vet[4]+5
print(senha)

		
