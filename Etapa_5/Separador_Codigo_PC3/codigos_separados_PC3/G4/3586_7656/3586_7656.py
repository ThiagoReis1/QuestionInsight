from numpy import*

vet = array(eval(input("Informe os valores: ")))
i = 0

acum = 0

while(i<size(vet)):
	if(vet[i] == 1):
		acum += 100
	elif(vet[i] == 2):
		acum += 60
	elif(vet[i] == 3):
		acum += 20
	else:
		acum += 0
	i += 1

print(acum)