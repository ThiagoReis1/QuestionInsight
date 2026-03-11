from numpy import *
vetor = array(eval(input()))
i = 0
ini = 200
while(i<size(vetor)):
	if(vetor[i]==1):
		ini = ini *4 
	elif(vetor[i]==2):
		ini = ini*2
	elif(vetor[i]==3):
		ini = ini
	elif(vetor[i]==4):
		ini = ini/2
	i = i + 1
print(round(ini,2))
		