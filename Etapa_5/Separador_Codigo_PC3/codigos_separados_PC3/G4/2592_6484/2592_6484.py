from numpy import*

v = array(eval(input()))
a = 0

for i in range(1,size(v)):
	if v[i] >= v[0]:
		print(i)
		a+=1
	
print(a)