from numpy import*
x=array(eval(input("x:")))
s=0
for i in range(size(x)):
	s=s+log(x[i]+1)
r=exp(s/size(x))
print(round(r-1,2))
