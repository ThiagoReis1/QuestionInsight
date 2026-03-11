from numpy import *

vetor = array(eval(input("Digite o vetor: ")))

tam = size(vetor)
zero = zeros(tam, dtype = int)

for i in range(tam):
	zero[i] = vetor[i] * 2
	
print(zero)