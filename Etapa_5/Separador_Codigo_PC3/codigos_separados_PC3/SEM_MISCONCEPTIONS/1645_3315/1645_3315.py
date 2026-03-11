from numpy import*

vetor = array(eval(input()))
cont = 0

for i in vetor:
	if i>=2000:
		cont = cont + 1
		
vetor2 = zeros(cont, dtype=int)

cont2 = 0

for j in range(0, size(vetor)):
	if vetor[j]>=2000:
		vetor2[cont2] = j
		cont2=cont2+1
		
print(cont)
print(vetor2)
