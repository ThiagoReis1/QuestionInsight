from numpy import*

vetor = array(eval(input("Digite as pontuações: ")))
R = 74.08
i = 0
cont = 0
while(i < size(vetor)):
	if(vetor[i] > R):
		cont = cont + 1
	i = i + 1
		
print(R)
print(cont)