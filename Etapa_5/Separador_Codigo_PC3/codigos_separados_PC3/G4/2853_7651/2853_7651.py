from numpy import*
v = array(eval(input()))
a = 0
for i in range(0,size(v)):
	if (v[i]==10):
		a = a *10
	else:
		a += v[i]
print(a)	
	
	