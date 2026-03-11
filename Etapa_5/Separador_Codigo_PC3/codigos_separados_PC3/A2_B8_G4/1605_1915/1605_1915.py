from numpy import*
vet = array(eval(input("")))
i = 0
p = 200
while(i < size(vet)):
	if(vet[i] == 1):
		p = p*4
	elif(vet[i] == 2):
		p = p*2
	elif(vet[i] == 3):
		p = p
	elif(vet[i] == 4):
		p = p/2
	i = i + 1	
print(round(p,2))	