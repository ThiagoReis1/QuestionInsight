from numpy import *
v= array(eval(input()))
resp=True
for i in range(len(v)-1):
	if v[i+1] < v[i]:
		resp=False	
print(resp)
