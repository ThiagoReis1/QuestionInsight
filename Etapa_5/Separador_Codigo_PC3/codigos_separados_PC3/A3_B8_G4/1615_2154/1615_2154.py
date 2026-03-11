from numpy import*

vet = array(eval(input("")))
vet2 = array(eval(input("")))

i = 0
p = 0
i2 = 0
p2 = 0

while(i < size(vet) or i2 < size(vet2)):
	if(vet[i] or vet2[i] == 1):
		p = p + 40
	elif(vet[i] == 2):
		p = p + 20
	elif(vet[i] == 3):
		p = p + 10
	elif(vet[i] == 4):
		p = p + 0
	i = i + 1 
