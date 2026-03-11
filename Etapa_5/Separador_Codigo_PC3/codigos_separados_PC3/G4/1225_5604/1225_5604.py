from numpy import*
from math import*
x=array(eval(input("vetor: ")))
n=size(v)
m=sum(v)/size(v)

for i in x:
	d=sqrt((i-m)**2)/n-1
	
print(round(d,3))