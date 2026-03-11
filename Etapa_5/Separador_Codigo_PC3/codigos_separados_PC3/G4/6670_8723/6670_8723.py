from numpy import *
v = array(eval(input(" ")))
md = zeros(size(v), dtype=float)
c = 0
for i in range(size(v)):
	if v[i] >20:
		md[i]=v[i]
		c= c+1
	else:
		md[i]= 0.0
		
if sum(md) == 0:
	print("0.0")
else:
	doce = sum(md)/c
	print(round(doce,2))
			 