from numpy import*

vet = array(eval(input("Insira os numeros dos aneis acertados: ")))
cont = 0
x = 0

while (cont < size(vet)):
	if (vet[cont] == 1):
		x = x + 80
	elif (vet[cont] == 2):
		x = x + 40
	elif (vet[cont] == 3):
		x = x + 20
	elif (vet[cont] == 4):
		x = x + 10
	cont = cont + 1
	
print(x)