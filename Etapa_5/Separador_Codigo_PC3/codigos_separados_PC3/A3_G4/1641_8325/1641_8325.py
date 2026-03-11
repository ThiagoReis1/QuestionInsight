from numpy import*

v=array(eval(input("n: ")))

c=0

n=zeros(v,dtype=int)
for c in range(size(v)):
	if(v%3==0):
		c=c+1
		v.append(c)
	print(c)

