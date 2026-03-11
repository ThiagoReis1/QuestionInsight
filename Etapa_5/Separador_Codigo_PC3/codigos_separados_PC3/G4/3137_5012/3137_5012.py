from numpy import*

v = eval(input("vetor:"))

i=0
c =0

while(i < size(v)):
	if(v[i]>=0):
		m = exp(v[i])/exp(size(v))
		c= c+ m
	i = i + 1	
print(round(log(c),2))