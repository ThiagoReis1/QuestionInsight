from numpy import*

v=array(eval(input()))
v1=0
v2=0
v3=0
v4=0
for i in range(size(v)):
	if v[i] == 1:
		v1 = v1 + 1
	elif v[i] == 2:
		v2 = v2+1
	elif v[i] == 3:
		v3 = v3+1
	elif v[i] == 4:
		v4 = v4+1
a = array([v1,v2,v3,v4])
print(a)
		