from numpy import*
vetor = array(eval(input("vetor de um numero: ")))
i = 0
cont = 0
while i < (size(vetor)):
	if vetor[i] == 1:
		cont = cont + 10
	elif vetor[i] == 2:
		cont = cont + 5
	elif vetor[i] == 3:
		cont = cont + 10
	elif vetor[i] == 4:
		cont = cont + 5
	elif vetor[i] == 5:
		cont = cont + 10
	elif vetor[i] == 6:
		cont = cont + 5
	i = i + 1
print(cont)

