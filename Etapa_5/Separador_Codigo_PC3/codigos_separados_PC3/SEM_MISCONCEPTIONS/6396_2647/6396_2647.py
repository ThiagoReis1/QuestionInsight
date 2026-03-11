from numpy import *

entrada = array(eval(input()))
vetor = zeros(len(entrada), dtype = int)
for i in range(len(entrada)):
	vetor[i]=entrada[i]*2

print(vetor)