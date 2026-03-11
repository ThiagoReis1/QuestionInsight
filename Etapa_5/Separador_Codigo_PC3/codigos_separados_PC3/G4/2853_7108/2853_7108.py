from numpy import*
v= array(eval(input()))
d=0
for i in range(size(v)):
	if v[i] == 10:
		d= d*10

	else:
		d= d + v[i]
		
print(d)
	
		
		