from numpy import*

v = array(eval(input()))
z=size(v)
s=zeros(z,dtype=int)
a=0
for i in v:
	if i==9:
		s[a]=0
	else:
		s[a]=(i+1)**3
	a+=1
print(s)