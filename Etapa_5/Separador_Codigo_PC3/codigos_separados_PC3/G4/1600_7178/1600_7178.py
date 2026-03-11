from numpy import*
x=array(eval(input("x")))
t=0
c=0
while(size(x)>c):
	if(x[c]>80):
		t=t+x[c]-(x[c]*0.15)
		c=c+1
	else:
		t=t+x[c]
		c=c+1
print(round(t,2))