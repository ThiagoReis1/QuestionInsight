from numpy import*

vet = array(eval(input()))
i = 0
aux = 200
while(i < size(vet)):
	if(vet[i] == 1):
		aux = aux * 4
	elif(vet[i] == 2):
		aux = aux * 2
	elif(vet[i] == 3):
		aux = aux 
	elif(vet[i] == 4):
		aux = aux / 2
	i = i + 1
print(aux)