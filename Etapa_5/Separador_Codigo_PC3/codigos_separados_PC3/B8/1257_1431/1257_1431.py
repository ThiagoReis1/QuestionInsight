from numpy import *
vetorinicial = array(eval(input("insira o valor do vetor:")))
A = min(vetorinicial)
B = max(vetorinicial)
C = 0.85 * A + 0.15 * B
D = 0.4 * A + 0.6 * B
vetorfinal = array([0 , 0])
for i in range(size(vetorinicial)):
	if (vetorinicial[i] >= A) and (vetorinicial[i] < C):
		vetorfinal[0] = vetorfinal[0] + 1
	elif (vetorinicial[i]>= D) and (vetorinicial[i] < B):
		vetorfinal[1] = vetorfinal[1] + 1
print(vetorfinal)