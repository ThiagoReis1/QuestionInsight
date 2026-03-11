from numpy import *

v=array(eval(input()))
p=0
i=0
for i in range(size(v)):
	if v[i]==1:
		p=p+80
	elif v[i] == 2:
		p=p+40
	elif v[i] == 3:
		p=p+20
	elif v[i] == 4:
		p=p+10
	i+=1
	d=sum(p)
print(d)
