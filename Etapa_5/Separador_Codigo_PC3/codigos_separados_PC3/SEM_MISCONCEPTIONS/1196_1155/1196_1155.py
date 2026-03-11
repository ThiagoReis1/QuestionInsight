from numpy import*
vetor1=array(eval(input("digite o vetor:")))
c1=0
pos=0
while(c1 < size(vetor1)):
	if(vetor1[c1]>60):
		pos=pos+1
	if (vetor1[c1]<-60):
	c1=c1+1
vetor2=array(zeros(pos,dtype=float))
c1=0
c2=0
while(c1<size(vetor1)):
	if(vetor1[c1]>60)or(vetor1[c1]>-60):
		vetor2[c2]=vetor1[c1]
		c2=c2+1
	c1=c1+1
print(vetor2)
		