from numpy import*

vet = array(eval(input("Digite o vetor: ")))
acum = 0
for i in range(size(vet)):
	if vet [i] >= 70: 
		acum = acum + 1
		
vet1 = zeros(acum, dtype=int)
j = 0
for i in range(size(vet)):
	if vet [i] >= 70:
		vet1 [j] = i
		j =j+1
print(acum)
print(vet1)