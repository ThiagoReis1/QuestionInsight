from numpy import*
v=array(eval(input()))
a=0
for i in range(size(v)):
	a=min(v)
b=sum(v)
b1=b-a

c=size(v)
c1=c-1
d=b1/c1
print(round(d,2))