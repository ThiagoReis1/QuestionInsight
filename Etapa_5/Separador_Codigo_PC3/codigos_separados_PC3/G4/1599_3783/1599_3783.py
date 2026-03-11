from numpy import *
p= array(eval(input("")))
v=0
for i in range(size(p)):
	if (p[i]<80):
		v+=p[i]
	else:
		v+=(p[i]/100)*85
print(round(v,2))	