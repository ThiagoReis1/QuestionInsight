from numpy import*
vet = array(eval(input("Informe o vetor de vendas: ")))         #Dica 1
total = 0	#Dica 2	   
zero = 0

for i in range(size(vet)):
	if(total <= 55):
		total = total + vet[i]
		
	else:
		total = zero + vet[i]
		
print(total)
	
	
	
	
	
	




	
		
	
	
