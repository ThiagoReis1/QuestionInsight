from numpy import *
a = input("digite: ").split(',')
v = zeros(5,dtype=int)
for i in range(size(a)):
	if(a[i] == "AR"):
		v[0] = v[0] + 1
	elif(a[i] == ("BR")):
		v[1] = v[1] + 1
	elif(a[i] == "CL"):
		v[2] = v[2] + 1
	elif(a[i] == "CO"):
		v[3] = v[3] + 1
	elif(a[i] == "UY"):
		v[4] = v[4] + 1
print(max(v))
print(v)