from numpy import*
vet = array(eval(input("temperaturas:")))
a=0
b=0

while(a<size(vet)):
	if(vet[a]>-100 or vet[a]==-100):
		b=b+1
	a=a+1
	
vet1 = array(zeros(b, dtype = float))
a=0
c=0

while(c<size(vet1)):
	if(vet[a]<-100):
		a=a+1
	else:
		vet1[c]=vet[a]
		c=c+1
		a=a+1
print(vet1)