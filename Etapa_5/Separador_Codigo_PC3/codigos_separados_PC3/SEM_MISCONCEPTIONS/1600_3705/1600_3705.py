from numpy import*
vetor=array(eval(input()))
i=0
desconto=vetor[i]//100*15
while(i<size(vetor)):
	for x in vetor:
		if(x>80):
			x=desconto
		elif(x<80):
			x=vetor[i]
		i=i+1
	i=i+1
print(round(sum(x,2))