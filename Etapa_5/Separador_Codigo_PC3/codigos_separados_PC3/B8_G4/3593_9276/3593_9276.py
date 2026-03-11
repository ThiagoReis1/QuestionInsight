from numpy import*

j=array(eval(input("")))
		
i=0
p=200

while i < size(j):
	if j[i]==1 or j[i]==3 or j[i]==5:
		p+= j/2
		
	elif j[i]==2 or j[i]==4 or j[i]==6:
		p+= j*3
		
	i+=1
	
print(round(p,2))