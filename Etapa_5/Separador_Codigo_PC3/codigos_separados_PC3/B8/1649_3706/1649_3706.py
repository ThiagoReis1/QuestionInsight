from numpy import*
from numpy.linalg import*

cor = input("")
vetor = cor.split(",")
cores= array([0,0,0,0,0])
i = 0 
while( i != size(vetor)):
	if(vetor[i] == "P"):
		cores[0] = cores[0] + 1
		i = i + 1
	elif(vetor[i] == "C"):	
		cores[1] = cores[1] + 1
		i= i +1
	elif(vetor[i] == "M"):	
		cores[2] = cores[2] + 1
		i= i +1
	elif(vetor[i] == "V"):	
		cores[3] = cores[3] + 1
		i= i +1
	elif(vetor[i] == "A"):	
		cores[4]=cores[4]+ 1	
		i= i +1
#1-p
#2-c
#3-m
#4-v
#5-a

print(max(cores))
print(cores)

