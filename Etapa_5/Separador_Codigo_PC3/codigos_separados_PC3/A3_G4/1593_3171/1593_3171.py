from numpy import * 

vet = array(eval(input("Informe as notas do trabalho: ")))

i = 0

soma = 0

k = 1

mult = []

v = []

while(i < size(vet)):
	
	soma = soma + (vet[i]*k)
	
	i = i + 1
	
	k = k + 1
	
	v.append(k + i - 1)
	
print(round(soma/max(v), 2))

