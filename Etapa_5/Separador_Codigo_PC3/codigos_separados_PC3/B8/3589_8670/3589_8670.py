from numpy import *

vet = array(eval(input("Informe os aneis acertados: ")))

i =  0
total = 0

while i < size(vet): 
	
	if vet[i] == 1:
		total = total + 80
		
	elif vet[i] == 2:
		total = total + 40
		
	elif vet[i] == 3:
		total = total + 20
		
	elif vet[i] == 4:
		total = total + 10
		
	i = i + 1
	
print(total)