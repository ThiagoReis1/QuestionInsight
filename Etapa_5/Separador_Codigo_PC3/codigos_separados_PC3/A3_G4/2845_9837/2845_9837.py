from numpy import *
r = array(eval(input("insira um numero:")))
i = 0

for x in range(0, size(r),1):
	if r[x] == 9:
	   r[x]= 0
	else:
		r[x]+= 1
print(r)
