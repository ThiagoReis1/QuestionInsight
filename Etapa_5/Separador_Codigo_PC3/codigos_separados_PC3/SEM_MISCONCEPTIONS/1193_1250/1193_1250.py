from numpy import*
vetor = array(eval(input("Digite o vetor: ")))
i = 0
count = 0
while(i<size(vetor)):
	while(vetor[i]<=-100):
		i = i + 1
		count = count + 1
	else:
		count = count + 1
	i = i + 1
print(vetor)
		
	
