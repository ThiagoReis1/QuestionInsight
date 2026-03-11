from numpy import*
from math import*
x=array(eval(input("x:")))
m=0
a=0
for i in range(size(x)):
	m=m+log(x[i]+1)
r=exp(m/size(x))
print(round(r-1,2))
