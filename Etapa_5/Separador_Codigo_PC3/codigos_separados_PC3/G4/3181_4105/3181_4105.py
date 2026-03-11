from numpy import*
v=array(eval(input()))
x=zeros(37,dtype=int)
for i in v:
	x[i]+=1
print(x)