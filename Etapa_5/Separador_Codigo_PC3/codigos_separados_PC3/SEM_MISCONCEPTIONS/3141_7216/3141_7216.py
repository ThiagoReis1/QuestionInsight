from numpy import*

vetor = array(eval(input()))

M = 0

for i in range(size(vetor)):
	M=M+vetor[i]**(1/6)
	
M = M/size(vetor)
M = M**6

print(round(M,2))