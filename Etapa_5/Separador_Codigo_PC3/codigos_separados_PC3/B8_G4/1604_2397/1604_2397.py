from numpy import*
v=array(eval(input()))
i=0
s=0
while(i<size(v)):
	if(v[i]==1):
		s=s+80
	elif(v[i]==2):
		s=s+40
	elif(v[i]==3):
		s=s+20
	elif(v[i]==4):
		s=s+10
	i=i+1
print(s)
