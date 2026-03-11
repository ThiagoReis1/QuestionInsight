from numpy import*
vetor = array(eval(input()))
p=sum(vetor)
lado=0
i=0
while(i<size(vetor)):
	if(vetor[i]>=5):
		lado=lado+1
	i=i+1
print(p)
print(lado)