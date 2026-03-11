from numpy import*
v= input()
a=input("")
c=0
while(c < size(v)):
	v[c]=v[c].replace("L", "R")
	if(v[c]==a):
		print(c)
	c=c+1