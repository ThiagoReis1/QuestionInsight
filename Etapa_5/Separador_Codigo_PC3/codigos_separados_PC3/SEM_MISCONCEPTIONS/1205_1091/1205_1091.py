from numpy import*
vetor= array(eval(input("Digite o vetor: ")))
recorde= 8.95
print(recorde)
i=0
while (i<=size(vetor)):
	
	if (vetor[i]>recorde):
		print(i)
	i=i+1