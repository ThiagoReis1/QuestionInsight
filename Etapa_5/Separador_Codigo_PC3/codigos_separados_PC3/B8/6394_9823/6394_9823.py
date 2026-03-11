from numpy import*

senha = array(eval(input()))
vetor = zeros(size(senha), dtype=int)

for i in range(0, size(senha)):
	vetor[i] = senha[i] + 1
	if senha[i] == 0:
		vetor[i] = senha[i] + 1
	elif senha[i] == 9:
		vetor[i] = senha[i] - 9

print(vetor)