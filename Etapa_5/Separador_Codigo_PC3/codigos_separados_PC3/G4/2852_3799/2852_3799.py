from numpy import*
x=array(eval(input("x:")))
s=0
for i in range(size(x)):
	if(x[i]!=88):
		s=s+x[i]
	else:
		s=s/2
print(s)
		
		