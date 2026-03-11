from numpy import*

v=array(eval(input("nota final:"))) 
c=0
d=0

for i in range(size(v)):
	if v[i] >= 5:
		c = c + 1
v1=zeros(c, dtype=int)

for x in range(size(v)):
	if v[x] >= 5:
		v1[d] = x
		d = d + 1 
		
print(c)
print(v1)
	