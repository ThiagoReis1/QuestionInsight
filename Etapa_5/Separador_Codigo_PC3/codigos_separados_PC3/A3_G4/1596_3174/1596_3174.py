from numpy import *

vet = array(eval(input("Informe as notas dos trabalhos: ")))

i = 0

soma = 0

k = 1

mult = []

while(i < size(vet)):
	
	soma = soma + (vet[i]*k)
	
	i = i + 1
	
	k = k + 1
	
print(round(soma, 2))
	
vet = [1, 2, 3]


	
	