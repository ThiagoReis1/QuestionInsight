from numpy import*
c= array(eval(input("vetor de custos dos intens:")))

i=0
while(i<size(c)):
	if(c[i] > 90.00):
		c[i]= c[i] - 6.50
	else:
		c[i]=c[i]
	i= i + 1
	total= sum(c)
print (round(total,2))