from numpy import*
v= array(eval(input()))
s= 0

for i in range(size(v)):
	if(v[i]!=0):
		s= s + v[i]
	else:
		s = 0
print(s)