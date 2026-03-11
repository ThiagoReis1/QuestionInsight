from numpy import*

v= array(eval(input()))

#x=zeros(0, dtype=int)
x=0

for i in range(1,len(v)):
	if(v[i] >= v[0]):
		print(i)
		x=x+1
print(x)
