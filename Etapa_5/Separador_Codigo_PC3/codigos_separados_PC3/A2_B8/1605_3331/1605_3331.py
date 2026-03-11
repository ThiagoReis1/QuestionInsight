from numpy import*

vetor= array(eval(input("Digite: ")))

i= 0
cont= 200

while (i < size(vetor)):
	if vetor[i] == 1:
		cont= cont * 4
	elif vetor[i] == 2:
		cont= cont * 2
	elif vetor[i] == 3:
		cont= cont
	elif vetor[i] == 4:
		cont= cont / 2
	i = i + 1
print(round(cont, 2))