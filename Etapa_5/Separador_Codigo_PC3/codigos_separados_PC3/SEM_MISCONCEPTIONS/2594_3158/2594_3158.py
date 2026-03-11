from numpy import*

vetor = array(eval(input("")))
cont = 0
for i in range(size(vetor)):	
	if vetor[i] > vetor[0]:
		cont=cont +1
		print(i)
	
print(cont)
	