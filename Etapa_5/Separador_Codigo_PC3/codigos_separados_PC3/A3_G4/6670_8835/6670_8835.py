from numpy import *
p = array(eval(input("")))
o = 0
q = 0
n = 0.0
for i in range(size(p)):
	if p[i] > 20:
		o = o + p[i]
		q+=1
	else:
		n = 0.0
if q > 0:
	cal = o/q
	print(round(cal,2))
else:
	print(n)