from numpy import*

vet = array(eval(input("Insira os valores: ")))
cont = 0
x = 0
total = 0
while (cont < size(vet)):
	x = x + (vet[cont]**(1/3))
	cont = cont + 1
	
total = (x / size(vet))**3
print(round(total,2))