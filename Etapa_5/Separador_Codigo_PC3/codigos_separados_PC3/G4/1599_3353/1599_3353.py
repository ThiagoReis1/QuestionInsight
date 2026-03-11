from numpy import*

cust=array(eval((input("digite um vetor: "))))
i=0
while(i<size(cust)):
	if(80<cust[i]):
		cust[i]=cust[i]*0.85
	i=i+1

print(round(sum(cust),2))