from numpy import *
sorotipos = array(eval(input("tipos")))
vetor = zeros(4,dtype=int)
for i in range(size(sorotipos)):
	if sorotipos[i] == 1:
		vetor[0] = vetor[0] + 1
	if sorotipos[i] == 2:
		vetor[1] = vetor[1] + 1
	if sorotipos[i] == 3:
		vetor[2] = vetor[2] + 1
	if sorotipos[i] == 4:
		vetor[3] = vetor[3] + 1

print(vetor)