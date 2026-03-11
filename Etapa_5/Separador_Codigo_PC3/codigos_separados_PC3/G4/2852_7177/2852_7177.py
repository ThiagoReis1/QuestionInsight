from numpy import*
u=array(eval(input("")))
f=0
for i in range(size(u)):
	if(u[i]!=88):
		f=f+u[i]
	else:
		f=f/2
print(f)