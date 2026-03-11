from numpy import*
v =eval(input())
a=0
s=0
for i in range(size(v)):
	s= v[i]+s
	if(v[i]>=5):
		a =a+1
print(s)
print(a)