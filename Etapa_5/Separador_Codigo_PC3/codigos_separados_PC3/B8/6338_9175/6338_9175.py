from numpy import * 

vetor = array(eval(input("Digite o vetor maiores que 8: ")))
				  
N = int(input("Digite um numero inteiro N: "))
	
quantidade = 0
					
for i in range(size(vetor)):
	if vetor[i] == N:
		print(i)
	elif vetor[i] > N:
		quantidade +=1
				
print(quantidade)
