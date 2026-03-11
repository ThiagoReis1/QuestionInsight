# Paulo Bitencourt
#11 - 08 - 2016

from numpy import*

vetor = array(eval(input("Digite o vetor: ")))

#record mundial
record = 307 
print (record)

i = 0
count = 0

while (i < size(vetor)):
	if (vetor[i] > record):
		count = count + 1 
	i = i + 1 
	
print (count)