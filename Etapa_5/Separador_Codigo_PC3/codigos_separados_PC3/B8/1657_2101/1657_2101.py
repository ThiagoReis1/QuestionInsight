from numpy import*

vetor = input(" estado:").upper().split(",")
estado = zeros (5 ,dtype =int)


for i in range(size(vetor)):
	if (vetor[i] == "AZ"):
		estado[0]= estado[0]+1
		
	elif (vetor[i] == "CA"):
		estado[1] = estado[1] +1
		
	elif (vetor[i] == "FL"):
		estado[2] = estado[2] +1
	
	elif (vetor[i] == "PA"):
		estado[3] = estado[3]+1
	
	elif (vetor[i] == "WI"):
		estado[4] = estado[4]+1

print (max(estado))
print(estado)



				  