from numpy import*

vet = array(eval(input()))

i = 0
aux = 0

while(i < size(vet)):  
	if(vet[i] == 1):       
		aux = aux + 80      
			
	elif(vet[i] == 2):
		aux = aux + 40
		                    
	elif(vet[i] == 3):           
		aux = aux + 20          
		                       
	elif(vet[i] == 4):
		aux = aux + 10
	i = i + 1
	
print(aux)