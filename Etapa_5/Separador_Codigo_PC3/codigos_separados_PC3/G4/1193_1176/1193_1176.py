from numpy import*
vet1= array(eval(input("digite as temperaturas: ")))
c1=0
pos=0
while (c1<size(vet1)):
	if (vet1[c1] > -100):
		pos= pos+1
	c1=c1+1
vet2= array(zeros(pos, dtype=float))	
c1=0
c2=0
while (c1<size(vet1)):
	if ((vet1[c1])>-100):
		vet2[c2]=vet1[c1]
		c2=c2+1
	c1=c1+1
print (vet2)