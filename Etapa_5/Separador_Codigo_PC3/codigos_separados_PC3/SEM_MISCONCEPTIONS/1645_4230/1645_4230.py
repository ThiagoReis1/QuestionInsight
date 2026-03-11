from numpy import*
val = array(eval(input("Valores sacados: ")))
saques = 0
for i in range(size(val)):
	if val[i] >= 2000 :
		saques = saques + 1
print(saques)
########################################certo#################################################
vetor = zeros(saques,dtype=int)
k = 0 
j = 0
for i in range(size(val)) :
	if val[i] >= 2000:
		vetor[k] = vetor[k] + j
		k = k + 1
	j = j + 1
print(vetor)