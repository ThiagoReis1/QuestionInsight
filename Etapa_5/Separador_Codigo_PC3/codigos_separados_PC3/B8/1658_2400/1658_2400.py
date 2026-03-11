from numpy import*
vetor = input().split(",")
vetorf=array([0,0,0,0,0])
i=0
while(i<size(vetor)):
	if(vetor[i]=="CHN"):
		vetorf[0]=vetorf[0]+1
		i=i+1
	elif(vetor[i]=="JPN"):
		vetorf[1]=vetorf[1]+1
		i=i+1
	elif(vetor[i]=="KOR"):
		vetorf[2]=vetorf[2]+1
		i=i+1
	elif(vetor[i]=="MGL"):
		vetorf[3]=vetorf[3]+1
		i=i+1
	elif(vetor[i]=="THA"):
		vetorf[4]=vetorf[4]+1
		i=i+1
l=max(vetorf)
print(l)
print(vetorf)