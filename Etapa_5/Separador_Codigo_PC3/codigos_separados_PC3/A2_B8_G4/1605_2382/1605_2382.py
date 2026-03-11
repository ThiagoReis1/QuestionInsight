from numpy import *
v=array(eval(input()))
i=0
s=200
while(i<size(v)):
	if(v[i]==1):
		s=s*4.0
	elif(v[i]==2):
		s=s*2.0
	elif(v[i]==3):
		s=s
	elif(v[i]==4):
		s=s/2
	#print(s)
	i=i+1
	
	
print(round(s,2))



