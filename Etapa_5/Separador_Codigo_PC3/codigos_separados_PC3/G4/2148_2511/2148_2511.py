#Lados e Perimetro de um poligono

from numpy import*

vet = array(eval(input("Primeiro vetor: ")))
cont = 0
for elemento in vet:
	if (elemento >=  5):
		cont = cont + 1 
print (sum(vet))
print (cont)
	
	
		