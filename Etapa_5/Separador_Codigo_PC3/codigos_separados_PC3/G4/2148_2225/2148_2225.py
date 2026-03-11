from numpy import*
v=array(eval(input("v: ")))

x=sum(v)
print(x)
c=0
for i in range(size(v)):
	if v[i]>=5:
		c=c+1
print(c)
	