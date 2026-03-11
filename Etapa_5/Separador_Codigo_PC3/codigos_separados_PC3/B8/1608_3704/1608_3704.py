from numpy import*
vetor = array(eval(input('vetor: ')))
t = 0
i = 0
#cada i é uma parada e ele indica a quantidade de pessoas que entraram ou sairam
while (i < size(vetor)) :
	t = t + vetor[i]
	if (t < 75) :
		i = i + 1
	elif (t > 75) :
		t = 75
		i = i + 1	
print(int(t))
	
	
		