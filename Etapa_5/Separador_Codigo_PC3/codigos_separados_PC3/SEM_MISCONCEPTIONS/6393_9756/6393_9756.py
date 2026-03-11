from numpy import *
numb = array(eval(input("informe a senha: ")))
vetor = zeros (size(numb), dtype = int)

for i in range (0, size(numb)):
	vetor[i] = ((numb[i]+1)**3)
	if numb[i] == 9:
		vetor[i] = 0
print (vetor)