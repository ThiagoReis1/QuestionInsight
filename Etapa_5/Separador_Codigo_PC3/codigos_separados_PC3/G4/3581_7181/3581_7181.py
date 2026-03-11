from numpy import*

v=array(eval(input(" ")))
s=0
i=0
while(i<size(v)):
	if(v[i]>40):
		s=s+(v[i]-2.5)
	else:
		s=s+v[i]
	i=i+1
	
print(round(s, 2))