from numpy import*
v=array(eval(input(": ")))
for i in range(0,size(v)):
	if(v[i]==9):
		v[i]=0
	else:
		v[i]=v[i]+1
print(v)