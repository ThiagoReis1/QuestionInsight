from numpy import *
v= array(eval(input('')))

for i in range(size(v)):
	if(v[i] == 0):
		v[i]=(v[i]+9)**2
	elif(v[i] != 0):
		v[i]=(v[i]-1)**2
print(v)