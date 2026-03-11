from numpy import*

vetor = array(eval(input("digite o valor: ")))
saida = zeros(size(vetor),dtype=int)
for i in range (size(vetor)):
	if (vetor[i] == 9): 
		saida[i] = 0
	else:  
		saida[i] = vetor[i] + 1
	
print(saida)