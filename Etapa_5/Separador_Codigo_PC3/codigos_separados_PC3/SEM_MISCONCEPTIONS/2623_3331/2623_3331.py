from numpy import*
from numpy.linalg import*

mat= array(eval(input("Digite: ")))
linha= shape(mat)[0]

vet= zeros(linha)


for i in range(linha):
	vet[i]= min(mat[i,:])

	
for i in range(size(vet)):
	if vet[i] == min(vet):
		print(i)

	
	
	
