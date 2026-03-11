from numpy import* 

carta = input().upper().split(',')


vet = zeros(4 , dtype = int) 

for i in carta: 
	if i == "C":  
		vet[0] += 1 
		
	elif i == "O": 
		vet[1] +=1 

	elif i == "P": 
		vet[2] +=1 
			
	elif i == "E": 
		vet[3] +=1 
			
print(vet)
		



