from numpy import*

vet1 = array(eval(input()))
vet2 = array(eval(input()))

i = 0 
dano = 0 

while(i < size(vet1)): 
	if(vet1[i] == "CENOURA"):
		dano = dano + (2*vet2[i])
	elif(vet1[i] == "FERRO"):
		dano = dano + (4*vet2[i])
	elif(vet1[i] == "DWARVEN"):
		dano = dano + (8*vet2[i])
	elif(vet1[i] == "ELVEN"):
		dano = dano + (11*vet2[i])
	else:
		dano = dano + (14*vet2[i])
		
	i = i + 1
	
print(round(dano,2))