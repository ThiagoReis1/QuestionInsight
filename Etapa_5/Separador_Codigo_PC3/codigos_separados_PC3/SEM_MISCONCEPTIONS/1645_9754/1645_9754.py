from numpy import*
saques = array(eval(input()))
cont = 0
for i in range(size(saques)):
	
	if saques[i]>=2000:
		cont += 1
vetor = zeros(cont,dtype=int)
j = 0
for i in range(size(saques)):
	if saques[i]>=2000:
		vetor[j]=i
		j = j +1
		
print(cont)
print(vetor)
	