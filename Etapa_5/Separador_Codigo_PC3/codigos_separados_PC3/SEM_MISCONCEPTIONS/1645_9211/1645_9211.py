from numpy import * 
vetor = array(eval(input("v:")))
cont = zeros(size(vetor),dtype=int)
for i in (size(vetor)):
	if vetor[i] >= 2000:
		cont[i] = cont[i] + 1
		print(size(cont))