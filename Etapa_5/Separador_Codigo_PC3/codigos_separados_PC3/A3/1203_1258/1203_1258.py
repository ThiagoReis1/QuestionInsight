from numpy import*
vetor = array(eval(input("digite o vetor:")))
record = 2.5
i = 0
cont = 0 
while(i < size(vetor)):
	if(vetor[1]>= record):
		cont = vetor[i] + 1 
	i = i + 1
else:
	print(record)
i = 0 
cont = 0
while(i<size(vetor)):
	if(vetor[i] > record):
		cont = cont + 1 
	i = i + 1 
print(cont)		