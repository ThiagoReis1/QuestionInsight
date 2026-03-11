from numpy import *
v = array(eval(input(":")))
i = 0
for i in range(size(v)):
	if(v[i]== 9):
		v[i] = 0
	else:
		v[i] = v[i] + 1
	i = i+1

		
print(v)
	

