from numpy import * 

vet = array(eval(input("Numero de ALunos: ")))

cont = 0
j = 0

for i in range(size(vet)):
	if(vet[i] % 5 == 0):
		cont = cont + 1
		
p = zeros(cont, dtype=int)

for i in range(size(vet)):
	if (vet[i] % 5 == 0):
		p[j] =i
		j = j + 1
		
print(cont)
print(p)