from numpy import*
n=array(eval(input("qul o vetor: ")))
i=0
d=0
while(i<size(n)):
	if(n[i]>80.0):
		n[i]=round(n[i]-5,2)
	i=i+1
a=sum(n)
print(round(a,2))