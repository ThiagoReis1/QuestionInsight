from numpy import *

vetor = array(eval(input("Digite o valor da mensagem: ")))
i = 0

for i in range(size(vetor)):
	vetor[i] = vetor[i] * 2
print(vetor)