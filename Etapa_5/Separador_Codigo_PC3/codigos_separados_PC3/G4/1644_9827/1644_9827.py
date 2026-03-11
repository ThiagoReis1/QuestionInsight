from numpy import*
notas = array(eval(input()))
acum = 0
for i in range(size(notas)):
	if	notas[i] < 5:
		acum +=1
print(acum)
vet = zeros(acum,dtype=int)
j=0

for i in range (size(notas)):
	if notas[i]<5:
		vet[j]= vet[j] + i
		j+=1
print(vet)
		
