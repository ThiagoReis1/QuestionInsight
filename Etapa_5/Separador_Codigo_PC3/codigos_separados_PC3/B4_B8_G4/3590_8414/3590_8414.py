from numpy import*

vet = array(eval(input(" insira o vetor: ")), dtype = int)
cont = 0

for i in vet: 
	if i == 1: 
		cont = cont + 10
	elif i == 2: 
		cont = cont + 5
	elif i == 3: 
		cont = cont + 0
	elif i == 4:
		cont = cont + 5
	elif i == 5:
		cont = cont + 20
	elif i == 6: 
		cont = cont + 10
print(cont)