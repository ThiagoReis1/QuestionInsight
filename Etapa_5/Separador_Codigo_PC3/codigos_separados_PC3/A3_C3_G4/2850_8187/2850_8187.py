from numpy import *
v= array(eval(input("")))
lim= 55
total=0
for i in range(size(v)):
	if(sum(v) < lim):
		cal= sum(v)
	total= total+1
	if(sum(v) > lim):
		cal= sum(v)-lim
	total=total+1
print(cal)