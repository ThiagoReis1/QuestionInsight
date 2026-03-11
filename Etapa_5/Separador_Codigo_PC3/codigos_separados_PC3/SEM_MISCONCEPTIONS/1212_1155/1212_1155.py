from numpy import*
vetor=array(eval(input("Digite o vetor:")))
recorde= 307
c=0
l=0
while(c < size(vetor)):
	if(vetor[c]<recorde):
		l=l+1
	c= c +1
print(recorde)
print(l)

	