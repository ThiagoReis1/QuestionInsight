from numpy import*
vetor = array(eval(input("Digite as distâncias: ")))
i = 0
s = 0
while(i < size(vetor)):
	if(vetor[i] > 2.5):
		s = s + 1
	i = i + 1	
print("2.5")
print(s)
