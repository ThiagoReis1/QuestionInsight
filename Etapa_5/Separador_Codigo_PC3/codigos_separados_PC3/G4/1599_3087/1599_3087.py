from numpy import*

c= array(eval(input("")))

d= zeros(size(c),dtype=float)

i=0
j=0


while(i<size(c)):
	if(c[i]>80):
		d[j]= c[i]-(15*c[i]/100)
	else:
		d[j]= c[i]
	i=i+1
	j=j+1


print(round(sum(d),2))	
		