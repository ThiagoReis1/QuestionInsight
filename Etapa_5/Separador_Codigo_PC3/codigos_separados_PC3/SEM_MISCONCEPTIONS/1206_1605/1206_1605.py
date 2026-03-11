from numpy import*
vetor = array(eval(input("Digite as distancias: ")))
i = 0 
s = 0 
while(i < size(vetor)):
	if(vetor[i] < 8.95):
		s = s + 1
	i = i + 1
print("8.95")
print(s)