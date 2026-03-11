from numpy import *

vn = array(eval(input()))
i = 0
vv = []

for e in range(size(vn)):
	
	if(vn[e]>=5):
		vv.append(e)
		i = i + 1
		

vv = array(vv)

print(i)
print(vv)