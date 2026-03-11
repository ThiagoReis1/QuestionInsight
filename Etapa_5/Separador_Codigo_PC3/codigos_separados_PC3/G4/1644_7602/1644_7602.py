from numpy import*

notas = array(eval(input()))

cont = 0
for i in range(size(notas)):
	if notas[i] < 5:
		cont += 1
		


vet = zeros(cont,dtype=int)
j = 0

for i in range(size(notas)):
	if notas[i] < 5:
		vet[j] = i
		j += 1
	
	
print(cont)
print(vet)
	
