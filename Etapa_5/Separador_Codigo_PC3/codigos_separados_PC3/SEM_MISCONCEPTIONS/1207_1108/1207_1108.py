from numpy import*
vetor = array(eval(input()), dtype = float)
i = 0
n = 0
recorde = 98.48
while(i < size(vetor)):
		if(vetor[i] > recorde):
			n = n + 1
		i = i + 1
print(recorde)
print(n)


	