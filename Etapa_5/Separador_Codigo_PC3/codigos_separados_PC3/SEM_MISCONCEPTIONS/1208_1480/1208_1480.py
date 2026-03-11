from numpy import*

vetor = array(eval(input("vetor: ")))
i = 0
maiores = 0 

while(i < size(vetor)):
	if(vetor[i] < 98.48):
		maiores = maiores + 1
	i = i + 1
print(98.48)
print(maiores)