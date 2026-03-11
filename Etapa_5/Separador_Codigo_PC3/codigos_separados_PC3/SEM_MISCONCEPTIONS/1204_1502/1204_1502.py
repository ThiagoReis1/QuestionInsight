from numpy import*
vetor = array(eval(input("informe as distancias: ")))
k = 0
i = 0
record = 2.5
while(i < size(vetor)):
	if(vetor[i] < record):
		k = k + 1
	i = i + 1
print(record)
print(k)