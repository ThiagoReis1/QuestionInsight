from numpy import*

vet1 = array(input()).upper()
vet2 = array(eval(input()))

i = 0

for i in range(vet1):
	if(vet1[i] == "GELO"):
		v = 2 * vet2[i]
		t = t + v
	elif(vet1[i] == "FOGO"):
		v = 3 * vet2[i]
		t = t + v
	elif(vet1[i] == "CHOQUE"):
		v = 4 * vet2[i]
		t = t + v
	elif(vet1[i] == "CONJURACAO"):
		v = 8 * vet2[i]
		t = t + v
	elif(vet1[i] == "ILUSAO"):
		v = 10 * vet2[i]
		t = t + v
	
print(t)		
	
		
		
	
	






