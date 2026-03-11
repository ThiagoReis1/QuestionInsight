from numpy import*

vetor = array(eval(input("Numeros inteiros: ")))

cont = zeros(vetor, dtype=int)

m = 0
for i in range(size(vetor)):
	if(vetor[i]!=1):
		cont[m] = i
		print(vetor)
		
print(cont)
		

	

		

